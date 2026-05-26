# 🔓 Checkmate - Kali Linux Online

A web-based interface to access and run Kali Linux commands and tools directly from your browser without downloading or installing anything.

## Features

✅ **Browser-Based Terminal** - Execute Kali Linux commands directly  
✅ **No Installation Required** - Run immediately in any browser  
✅ **Quick Tool Access** - One-click access to popular penetration testing tools  
✅ **System Commands** - List, navigate, and manage files  
✅ **Real-time Output** - See command results instantly  
✅ **Responsive Design** - Works on desktop and mobile  
✅ **Educational Focus** - Perfect for learning ethical hacking  

## Tools Included

- 🔍 **Nmap** - Port scanning and network mapping
- 📡 **Wireshark** - Packet analysis
- 📶 **Aircrack-ng** - WiFi security testing
- 💾 **SQLMap** - SQL injection testing
- 🔑 **John the Ripper** - Hash cracking
- 🔐 **Hashcat** - GPU-accelerated cracking

## Prerequisites

Before running this project, ensure you have:

- **Node.js** (v14 or higher) - [Download](https://nodejs.org/)
- **npm** (comes with Node.js)
- **Kali Linux** or a system with similar tools installed (or Docker container)
- **Git** (optional, for cloning)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/simonajay2007-prog/Checkmate-.git
cd Checkmate-
```

### 2. Install Dependencies

```bash
npm install
```

This will install:
- `express` - Web framework
- `body-parser` - Request parsing
- `nodemon` - Auto-restart during development

## Running the Application

### Start the Server

```bash
npm start
```

Or for development with auto-reload:

```bash
npm run dev
```

### Access the Application

Open your browser and navigate to:

```
http://localhost:3000
```

You should see the Kali Linux Online interface!

## Usage

### Method 1: Quick Tool Access
1. Click on any tool or command in the left sidebar
2. The command executes instantly
3. Results appear in the terminal

### Method 2: Manual Command Entry
1. Type your command in the input field at the bottom
2. Press **Enter** or click **Execute**
3. Output appears in the terminal above

### Example Commands

```bash
# Network reconnaissance
nmap -sV localhost
nmap -p 1-65535 target-ip

# System information
uname -a
ifconfig
whoami
pwd

# File management
ls -la
cat filename.txt

# DNS lookup
nslookup google.com
dig example.com

# Port scanning
netstat -tuln

# Process management
ps aux
kill -9 PID
```

## Project Structure

```
Checkmate-/
├── server.js          # Main Express server
├── package.json       # Project dependencies
├── README.md          # This file
└── public/
    └── index.html     # Web interface
```

## File Descriptions

### server.js
The main backend server using Express.js. It:
- Serves the web interface
- Handles command execution via `/execute` POST endpoint
- Manages stdin/stdout/stderr streams
- Includes error handling and timeouts

### public/index.html
The frontend web interface featuring:
- Terminal emulator display
- Command input field
- Sidebar with quick-access tools
- Real-time command output
- Responsive dark theme

### package.json
Node.js project configuration with:
- Dependencies (express)
- Dev dependencies (nodemon)
- NPM scripts (start, dev)

## Configuration

### Change Port

Edit `server.js` to use a different port:

```javascript
const PORT = process.env.PORT || 5000; // Change 3000 to your desired port
```

Or set environment variable:

```bash
PORT=5000 npm start
```

### Command Timeout

Adjust timeout in `server.js` (default 30 seconds):

```javascript
const cmd = spawn('bash', ['-c', command], {
    timeout: 60000 // Change to 60 seconds
});
```

## Troubleshooting

### Issue: "Command not found"
**Solution:** The tool is not installed on your system. Install it or use Docker.

### Issue: Port 3000 already in use
**Solution:** Use a different port:
```bash
PORT=3001 npm start
```

### Issue: Commands not executing
**Solution:** Check that your system has the required tools installed:
```bash
which nmap
which wireshark
```

### Issue: CORS or security errors
**Solution:** This is designed for local/internal networks only. For production, add authentication and rate limiting.

## Using with Docker

To run Kali Linux in Docker and connect this interface:

### 1. Pull Kali Linux Docker Image

```bash
docker pull kalilinux/kali-linux-docker
```

### 2. Run Container

```bash
docker run -it kalilinux/kali-linux-docker
```

### 3. Inside Container, Install Node.js

```bash
apt-get update
apt-get install -y nodejs npm
```

## Security Considerations

⚠️ **IMPORTANT:** This application executes system commands. Use it responsibly:

- ✅ Use only on **authorized systems** you own or have permission to test
- ✅ Use in **private networks** only
- ✅ Add **authentication** before production deployment
- ✅ Implement **rate limiting** to prevent abuse
- ❌ Do NOT use for unauthorized access
- ❌ Do NOT scan systems you don't own
- ❌ Do NOT use for malicious purposes

## Legal Notice

This tool is for **educational purposes only**. Unauthorized access to computer systems is illegal. Always:

1. Get explicit permission before testing
2. Follow all applicable laws and regulations
3. Use ethical hacking practices
4. Document all security testing activities

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Future Enhancements

- [ ] noVNC integration for GUI desktop access
- [ ] Multi-user support with sessions
- [ ] Command history and autocomplete
- [ ] File upload/download functionality
- [ ] Authentication system
- [ ] Docker container management
- [ ] Real-time collaborative terminal
- [ ] Custom command presets

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or suggestions:

1. Open an GitHub issue
2. Check the troubleshooting section
3. Review server logs for errors

## Credits

Built with:
- [Express.js](https://expressjs.com/) - Web framework
- [Kali Linux](https://www.kali.org/) - Penetration testing platform
- [Node.js](https://nodejs.org/) - JavaScript runtime

## Disclaimer

This project is provided as-is without warranty. Users are responsible for all actions taken with this tool. Always use ethically and legally.

---

**Made with ❤️ by Checkmate**

🔓 Try Kali Linux Online - No Download Required!
