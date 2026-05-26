# 🔓 Kali Linux Online

Try Kali Linux in your browser without downloading or installing anything locally!

## Features

✅ **No Download Required** - Access Kali Linux through your web browser  
✅ **Full Desktop Environment** - Complete GUI via VNC (noVNC)  
✅ **Pre-installed Tools** - Includes top 10 Kali tools, Metasploit, Nmap, Burp Suite  
✅ **Resource Limited** - 2GB RAM and CPU quota per session for safety  
✅ **Auto-timeout** - Sessions expire after 30 minutes of inactivity  
✅ **Multiple Sessions** - Support for concurrent users  
✅ **Easy Deployment** - Docker-based, cloud-ready  
✅ **Completely Isolated** - Each session runs in its own container  

## Quick Start

### Prerequisites
- Docker installed and running
- Python 3.7+
- Bash/Shell access

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/simonajay2007-prog/Checkmate-.git
   cd Checkmate-
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Build and deploy with Docker**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

   OR manually:
   ```bash
   docker build -t kali-linux-online .
   docker run -d --name kali-online-app -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock kali-linux-online python3 app.py
   ```

4. **Access the application**
   ```
   Open your browser and go to: http://localhost:5000
   ```

## How to Use

1. **Launch Session** - Click the "Launch Session" button to start a Kali Linux container
2. **Wait for Initialization** - The VNC server will initialize (usually 10-30 seconds)
3. **Connect to VNC** - Click "Connect to VNC" to open the desktop environment
4. **Use Kali Tools** - Access all installed tools from the terminal and GUI
5. **Stop Session** - Click "Stop Session" to terminate and clean up resources

## API Endpoints

### Create a Session
```bash
POST /api/session/create
```
Response:
```json
{
  "success": true,
  "session_id": "a1b2c3d4",
  "message": "Kali Linux session started successfully"
}
```

### Get VNC URL
```bash
GET /api/session/<session_id>/vnc-url
```
Response:
```json
{
  "success": true,
  "vnc_url": "http://localhost:6080/vnc.html"
}
```

### Stop a Session
```bash
POST /api/session/<session_id>/stop
```
Response:
```json
{
  "success": true,
  "message": "Session stopped"
}
```

### List Active Sessions
```bash
GET /api/sessions
```
Response:
```json
{
  "sessions": [
    {
      "session_id": "a1b2c3d4",
      "created_at": "2026-05-26T10:30:00",
      "last_activity": "2026-05-26T10:35:00",
      "status": "active"
    }
  ]
}
```

## File Structure

```
Checkmate-/
├── Dockerfile              # Kali Linux container definition
├── supervisord.conf        # Process management config
├── app.py                  # Flask backend application
├── requirements.txt        # Python dependencies
├── deploy.sh              # Deployment script
├── templates/
│   └── index.html         # Web interface
└── README.md              # This file
```

## Configuration

### Session Timeout
Edit `app.py` line 13 to change session timeout:
```python
KaliSession(session_id, timeout_minutes=30)  # Change 30 to desired minutes
```

### Resource Limits
Edit `app.py` lines 34-36 to adjust container resources:
```python
mem_limit='2g',      # Change to desired memory limit
cpu_quota=100000,    # Change to desired CPU quota
```

### Port Configuration
Edit `docker run` command or `deploy.sh` to change port:
```bash
-p 5000:5000  # Change first 5000 to your desired port
```

## System Requirements

- **OS**: Linux (recommended for Docker), Windows/Mac with Docker Desktop
- **RAM**: Minimum 4GB, recommended 8GB+
- **Storage**: 5-10GB for Kali Linux image
- **Network**: Stable internet connection
- **CPU**: 2+ cores recommended

## Cloud Deployment

### AWS EC2
```bash
# Launch an EC2 instance with Docker pre-installed
# Then run deploy.sh
```

### DigitalOcean
```bash
# Create a Droplet with Docker
# SSH into the droplet
# Clone and run deploy.sh
```

### Heroku
```bash
# Configure Procfile and deploy
heroku create
git push heroku main
```

## Security Considerations

⚠️ **Important**: This application is for educational purposes. When deploying:

1. **Use HTTPS** - Enable SSL/TLS for production
2. **Authentication** - Add user authentication for access control
3. **Rate Limiting** - Implement rate limiting to prevent abuse
4. **Firewall Rules** - Restrict access to trusted IPs
5. **Monitor Resources** - Track container resource usage
6. **Regular Updates** - Keep Kali Linux image updated

## Troubleshooting

### VNC Connection Issues
```bash
# Check if container is running
docker ps | grep kali-session

# Check logs
docker logs kali-session-<id>
```

### Docker Socket Permission Issues
```bash
# Ensure docker socket has correct permissions
sudo chown 666 /var/run/docker.sock
```

### Port Already in Use
```bash
# Find and stop the process using port 5000
lsof -i :5000
kill -9 <PID>
```

## License

This project is open source. Kali Linux is maintained by the Offensive Security team.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## Support

For issues and questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review official Kali Linux documentation

## Disclaimer

Kali Linux is provided for educational and authorized security testing only. Users are responsible for complying with all applicable laws and regulations. Unauthorized access to computer systems is illegal.
