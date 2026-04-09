#!/bin/bash

# --- S24 Custom Image Gen: Termux Setup (V2 - High Compatibility) ---
echo "--- Starting S24 Termux Setup (Optimized for 8GB RAM) ---"

# 1. Update and Enable TUR (Termux User Repository)
# This is crucial for pre-built PyTorch/AI libs on Android
echo "[1/4] Setting up Termux repositories..."
pkg update -y && pkg upgrade -y
pkg install -y tur-repo

# 2. Install Python & Optimized System AI Libs
# We use 'python-pytorch' from TUR because building from source on S24 is too slow/buggy
echo "[2/4] Installing Python and optimized AI libraries..."
pkg install -y python python-pip libjpeg-turbo libpng libwebp freetype libffi openssl build-essential clang rust cmake ninja git wget binutils ndk-sysroot
pkg install -y python-numpy python-pillow python-pytorch python-torchvision

# 3. Handle remaining dependencies via Pip
# We use --system because virtualenvs can be tricky with TUR system packages
echo "[3/4] Installing remaining dependencies..."
pip install diffusers transformers accelerate gradio --break-system-packages

# --- Final Check ---
if [ $? -eq 0 ]; then
    echo "--- Setup Complete! ---"
    echo "To start the app, run: bash start.sh"
else
    echo "--- Setup Failed! ---"
    echo "Tip: If it failed on 'pip', try running it again."
fi
