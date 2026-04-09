#!/bin/bash

# --- S24 Custom Image Gen: Termux Setup Script ---
echo "--- Starting S24 Termux Setup (Optimized for 8GB RAM) ---"

# 1. Update and Upgrade Packages
echo "[1/4] Updating Termux packages..."
pkg update -y && pkg upgrade -y

# 2. Install Python & Essential Build Tools
echo "[2/4] Installing Python and build dependencies..."
pkg install -y python python-pip libjpeg-turbo libpng libwebp freetype libffi openssl build-essential clang rust cmake ninja git wget binutils ndk-sysroot

# 3. Create & Activate Virtual Environment
echo "[3/4] Setting up Python environment..."
python -m venv venv
source venv/bin_activate

# 4. Install AI Libraries (CPU optimized for Mobile)
echo "[4/4] Installing AI libraries (this may take a few minutes)..."
pip install --upgrade pip
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install diffusers transformers accelerate gradio pillow numpy

# --- Final Check ---
if [ $? -eq 0 ]; then
    echo "--- Setup Complete! ---"
    echo "To start the app, run: bash start.sh"
else
    echo "--- Setup Failed! Check the error logs above. ---"
fi
