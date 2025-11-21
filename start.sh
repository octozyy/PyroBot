#!/bin/bash
# Start script for Vii Userbot

# Activate venv if exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install requirements if not done
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Run the bot
python3 -m PyroUbot