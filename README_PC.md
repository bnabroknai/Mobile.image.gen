# 🖥️ Personal Image Generator (PC/Chromebook Optimized)

This version is specifically designed for systems with **4GB of RAM** and **Intel/AMD CPUs** (like your AMD A4 Chromebook). It uses **OpenVINO** and **LCM (Latent Consistency Models)** to provide fast generation without crashing your hardware.

---

## 🛠️ Setup (Linux/Crostini/Ubuntu/Mint)

1. **Clone the Repo** (if you haven't):
   ```bash
   git clone <repo_url> && cd s24-image-gen
   ```

2. **Run the Setup Script**:
   This script will install dependencies and create a **12GB Swap File** (this is vital for 4GB systems).
   ```bash
   bash setup_pc.sh
   ```

---

## 🚦 How to Start the App

Once setup is complete, run:

```bash
bash start_pc.sh
```

The app will be available at: `http://localhost:7861`

---

## 🎨 PC Features
- **OpenVINO Acceleration**: Uses your AMD CPU more efficiently than standard PyTorch.
- **LCM-Distilled**: Generates high-quality images in just **4 to 8 steps**.
- **NSFW-Enabled**: Safety checkers are disabled by default.
- **Low Memory Mode**: Uses lazy-loading and aggressive memory management.

---

## 💡 Tips for the Chromebook 11a

### 1. The First Run
The very first time you generate an image, it will be **slow**. This is because OpenVINO is "compiling" the model to match your exact CPU. After the first image, subsequent generations will be much faster.

### 2. Steps vs. Quality
Since this uses an **LCM** model (Dreamshaper v7), you don't need 20-30 steps.
- **4 Steps**: Fast and good.
- **8 Steps**: Maximum quality.
- **12 Steps**: Overkill for this model.

### 3. Keep it Cool
AI generation is heavy on the CPU. Make sure your Chromebook has good airflow, as it will get warm during generation!

### 4. Swap Space
If the app ever crashes, check your disk space. The 12GB swap file needs enough room on your SSD to function.
