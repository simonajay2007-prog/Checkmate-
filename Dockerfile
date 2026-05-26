# Use official Kali Linux base image
FROM kalilinux/kali-linux-docker:latest

# Update and install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openssh-server \
    supervisor \
    xvfb \
    fluxbox \
    x11vnc \
    novnc \
    websockify \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Kali tools
RUN apt-get update && apt-get install -y \
    kali-tools-top10 \
    metasploit-framework \
    nmap \
    burp-suite-community \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -s /bin/bash kaliuser && \
    echo "kaliuser:kaliuser" | chpasswd && \
    usermod -aG sudo kaliuser

# Configure supervisor for services
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports
EXPOSE 5900 6080 22

# Start services
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]