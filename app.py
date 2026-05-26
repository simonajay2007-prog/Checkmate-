from flask import Flask, render_template, request, jsonify
import docker
import os
import uuid
import json
from datetime import datetime, timedelta

app = Flask(__name__)
client = docker.from_env()

# Store active sessions
active_sessions = {}

class KaliSession:
    def __init__(self, session_id, timeout_minutes=30):
        self.session_id = session_id
        self.container = None
        self.created_at = datetime.now()
        self.timeout = timedelta(minutes=timeout_minutes)
        self.last_activity = datetime.now()
    
    def start(self):
        """Start a new Kali Linux container"""
        try:
            self.container = client.containers.run(
                'kalilinux/kali-linux-docker:latest',
                detach=True,
                ports={'6080/tcp': None, '5900/tcp': None},
                environment=['DISPLAY=:99'],
                name=f'kali-session-{self.session_id}',
                mem_limit='2g',
                cpu_quota=100000,
                stdin_open=True,
                tty=True
            )
            return True
        except Exception as e:
            print(f"Error starting container: {e}")
            return False
    
    def is_expired(self):
        """Check if session has expired"""
        return datetime.now() - self.last_activity > self.timeout
    
    def get_vnc_url(self):
        """Get the VNC/noVNC connection details"""
        if not self.container:
            return None
        try:
            ports = self.container.ports
            vnc_port = ports['6080/tcp'][0]['HostPort']
            return f"http://localhost:{vnc_port}/vnc.html"
        except:
            return None
    
    def stop(self):
        """Stop and remove the container"""
        if self.container:
            try:
                self.container.stop(timeout=5)
                self.container.remove()
            except:
                pass

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/api/session/create', methods=['POST'])
def create_session():
    """Create a new Kali Linux session"""
    session_id = str(uuid.uuid4())[:8]
    session = KaliSession(session_id)
    
    if session.start():
        active_sessions[session_id] = session
        return jsonify({
            'success': True,
            'session_id': session_id,
            'message': 'Kali Linux session started successfully'
        }), 201
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to start Kali Linux session'
        }), 500

@app.route('/api/session/<session_id>/vnc-url', methods=['GET'])
def get_vnc_url(session_id):
    """Get VNC connection URL for a session"""
    session = active_sessions.get(session_id)
    
    if not session:
        return jsonify({'success': False, 'message': 'Session not found'}), 404
    
    if session.is_expired():
        session.stop()
        del active_sessions[session_id]
        return jsonify({'success': False, 'message': 'Session expired'}), 410
    
    session.last_activity = datetime.now()
    vnc_url = session.get_vnc_url()
    
    if vnc_url:
        return jsonify({'success': True, 'vnc_url': vnc_url}), 200
    else:
        return jsonify({'success': False, 'message': 'VNC URL not available yet'}), 202

@app.route('/api/session/<session_id>/stop', methods=['POST'])
def stop_session(session_id):
    """Stop a Kali Linux session"""
    session = active_sessions.get(session_id)
    
    if not session:
        return jsonify({'success': False, 'message': 'Session not found'}), 404
    
    session.stop()
    del active_sessions[session_id]
    
    return jsonify({'success': True, 'message': 'Session stopped'}), 200

@app.route('/api/sessions', methods=['GET'])
def list_sessions():
    """List all active sessions"""
    expired_sessions = []
    
    for session_id, session in active_sessions.items():
        if session.is_expired():
            session.stop()
            expired_sessions.append(session_id)
    
    for session_id in expired_sessions:
        del active_sessions[session_id]
    
    sessions_info = []
    for session_id, session in active_sessions.items():
        sessions_info.append({
            'session_id': session_id,
            'created_at': session.created_at.isoformat(),
            'last_activity': session.last_activity.isoformat(),
            'status': 'active'
        })
    
    return jsonify({'sessions': sessions_info}), 200

@app.errorhandler(404)
def not_found(e):
    return jsonify({'success': False, 'message': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)