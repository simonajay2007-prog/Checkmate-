const express = require('express');
const { spawn } = require('child_process');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Execute terminal commands
app.post('/execute', (req, res) => {
    const { command } = req.body;
    
    if (!command || command.trim() === '') {
        return res.status(400).json({ error: 'Command is required' });
    }
    
    const cmd = spawn('bash', ['-c', command], {
        timeout: 30000 // 30 second timeout
    });
    
    let output = '';
    let errorOutput = '';
    
    cmd.stdout.on('data', (data) => {
        output += data.toString();
    });
    
    cmd.stderr.on('data', (data) => {
        errorOutput += data.toString();
    });
    
    cmd.on('close', (code) => {
        res.json({
            output: output,
            error: errorOutput,
            code: code
        });
    });
    
    cmd.on('error', (err) => {
        res.status(500).json({ error: err.message });
    });
});

// Health check endpoint
app.get('/health', (req, res) => {
    res.json({ status: 'Server is running', timestamp: new Date() });
});

// Root route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`\n🔓 Kali Linux Online Server Running!`);
    console.log(`📍 Access at: http://localhost:${PORT}`);
    console.log(`\n⚠️  Warning: This server executes system commands.`);
    console.log(`   Use only in secure, controlled environments!\n`);
});