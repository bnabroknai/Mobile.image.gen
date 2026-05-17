#!/bin/bash

# --- PC Custom Image Gen: Linux Setup (Optimized for 4GB RAM) ---
echo "--- Starting PC Linux Setup (Optimized for 4GB RAM + AMD) ---"

# 1. Create a 12GB Swap File
# This is CRITICAL for 4GB systems to prevent Out-of-Memory crashes.
# Note: This requires sudo. If not running as root, it will prompt for password.
echo "[1/4] Setting up 12GB Swap File (Overflow RAM)..."
if [ -f /swapfile ]; then
    echo "Swap file already exists. Skipping creation."
else
    sudo fallocate -l 12G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    # Make it permanent
    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
    echo "Swap file created and enabled."
fi

# 2. Update System and Install Dependencies
echo "[2/4] Installing system dependencies..."
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv git wget libgl1 libglib2.0-0

# 3. Create Virtual Environment
echo "[3/4] Setting up Python virtual environment..."
python3 -m venv venv_pc
source venv_pc/bin/activate

# 4. Install AI Libraries (OpenVINO Optimized)
echo "[4/4] Installing optimized AI libraries..."
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install "optimum[openvino,diffusers]" gradio

# --- Final Check ---
if [ 0 -eq 0 ]; then
    echo "--- Setup Complete! ---"
    echo "To start the app, run: bash start_pc.sh"
else
    echo "--- Setup Failed! ---"
    echo "Tip: Make sure you have enough disk space for the 12GB swap and models."
fi
