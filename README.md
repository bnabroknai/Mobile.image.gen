# 🚀 S24 Personal Image Generator (NSFW Optimized)

A custom, on-device image generation tool for your **Samsung Galaxy S24 (8GB RAM)**. Run everything locally in Termux—no cloud, no censorship, full privacy.

---

## 🛠️ One-Command Setup (Paste in Termux)

```bash
pkg install git -y && git clone https://github.com/your-repo/s24-image-gen.git && cd s24-image-gen && bash setup.sh
```

---

## 🚦 How to Start the App

Once setup is complete, run this command whenever you want to start generating images:

```bash
bash start.sh
```

---

## 🎨 Features
- **Text-to-Image**: High-quality generation from your prompts.
- **Inpainting**: Edit specific parts of your images by painting a mask.
- **Mobile Optimized**: Uses attention slicing and low memory usage for 8GB RAM performance.
- **Privacy-First**: No internet required after the initial model download.
- **NSFW-Ready**: Safety checkers are disabled by default.

---

## 💡 Pro Tips for Best Quality

### 1. The Right Models
I've started you with **Stable Diffusion 1.5** (a solid all-rounder). To get high-quality realistic/NSFW results, I recommend downloading a specialized model from **Civitai** (e.g., *Realistic Vision V5.1* or *Pony Diffusion V6*).
- Download the `.safetensors` file.
- Update `MODEL_ID` in `app.py` to point to the file path.

### 2. S24 Performance Settings
- **Steps**: 15 to 20 is the sweet spot.
- **Resolution**: 512x512 (Standard) or 512x768 (Portrait). Going higher will slow down the generation on 8GB RAM.
- **Seed**: Use -1 for a random result every time.

---

## 🔒 Security & Safety
This tool is for personal use on your device. Always respect local laws and ethical guidelines regarding generated content.
