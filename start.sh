#!/bin/bash

# --- S24 Custom Image Gen: Startup Script ---

# 1. Activate Environment
if [ -d "venv" ]; then
    echo "--- Activating Python Environment... ---"
    source venv/bin/activate
else
    echo "--- Error: venv not found. Run bash setup.sh first! ---"
    exit 1
fi

# 2. Start Application
echo "--- Launching S24 Personal Image Generator... ---"
echo "Note: The first run will download models (around 2-3GB). This may take a few minutes."
python app.py
