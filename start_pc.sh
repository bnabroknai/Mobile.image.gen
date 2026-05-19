#!/bin/bash

# --- PC Custom Image Gen: Startup Script ---

echo "--- Launching PC Personal Image Generator... ---"
echo "Note: The first run will take several minutes to download and compile the model for your CPU."

# Activate the PC-specific environment
source venv_pc/bin/activate

# Run the PC app
python3 app_pc.py
