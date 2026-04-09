#!/bin/bash

# --- S24 Custom Image Gen: Startup Script ---

# Start Application
echo "--- Launching S24 Personal Image Generator... ---"
echo "Note: The first run will download models (around 2-3GB). This may take a few minutes."

# Run directly using system python since we used --break-system-packages for stability
python app.py
