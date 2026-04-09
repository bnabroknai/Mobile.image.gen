# 📄 S24 Personal Image Gen: Cheat Sheet

A quick guide for commands and best practices on your S24.

---

## 🏃 Quick Commands

| Action | Command |
| :--- | :--- |
| **Start the App** | `bash start.sh` |
| **Activate Environment** | `source venv/bin/activate` |
| **Stop the App** | Press `Ctrl + C` in Termux |
| **Update the Repo** | `git pull` |
| **Reset Everything** | `rm -rf venv && bash setup.sh` |

---

## 🎨 Best Prompt Formulas

### For Realistic Quality (NSFW/SFW)
- **Positive Prompt**: `(photorealistic, raw photo, highly detailed, 8k, masterpiece:1.2), [subject], [pose], [outfit], soft lighting, film grain, Fujifilm XT3.`
- **Negative Prompt**: `(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation.`

---

## ⚙️ S24 Settings (Optimized for 8GB RAM)

| Setting | Recommended Value | Why? |
| :--- | :--- | :--- |
| **Resolution** | `512x512` | Best for speed and memory. |
| **Sampling Steps** | `15 - 20` | Good balance of quality. |
| **Guidance Scale** | `7.0 - 8.5` | Standard for most models. |
| **Low VRAM Mode** | `Enabled` | `app.py` already handles this! |

---

## 📂 Troubleshooting

### 1. "Out of Memory" (OOM)
- Close other apps on your S24 before starting Termux.
- Keep resolution at 512x512.
- If it persists, restart Termux completely.

### 2. Slow Generation
- Ensure your phone isn't in "Power Saving Mode."
- Keep the S24 cool (AI generation makes it warm!).
- 8GB RAM is enough for SD 1.5, but SDXL will be much slower.

### 3. "Port Already in Use"
- Run `fuser -k 7860/tcp` to clear the port.

---

## 🚀 Future Upgrades
Once you're comfortable, ask me how to:
1. **Load specialized NSFW models** (.safetensors).
2. **Add LoRA support** (for specific people or styles).
3. **Speed up generation** with ONNX/OpenCL.
