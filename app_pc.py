import os
import gradio as gr
import torch
import numpy as np
from optimum.intel.openvino import OVStableDiffusionPipeline
from diffusers import LCMScheduler

# --- PC Configuration (Optimized for 4GB RAM + AMD CPU) ---
# We use an LCM-distilled model for maximum speed on weak hardware
MODEL_ID = "SimianLuo/LCM_Dreamshaper_v7"
DEVICE = "CPU" # OpenVINO CPU is most stable for 4GB systems

pipe = None

def load_pipeline():
    global pipe
    if pipe is None:
        print("Loading OpenVINO Optimized LCM Model (This may take a moment)...")
        # Load with OpenVINO acceleration
        # 'export=True' will convert the model to OpenVINO IR format on the first run
        pipe = OVStableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            export=True,
            device=DEVICE,
            compile=True
        )
        # Use LCM Scheduler for fast inference (1-8 steps)
        pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)

        # Disable safety checker for NSFW support as requested
        # In optimum-intel, we can just set it to None if it exists
        if hasattr(pipe, "safety_checker"):
            pipe.safety_checker = None

        print("Model loaded successfully!")

def generate(prompt, neg_prompt, steps, scale, seed, height, width):
    load_pipeline()

    # Handle random seed
    if seed == -1:
        seed = np.random.randint(0, 2**32 - 1)

    # Set seed for reproducibility
    np.random.seed(int(seed))

    # LCM models perform best with low guidance scale (1.0 - 2.0)
    image = pipe(
        prompt=prompt,
        negative_prompt=neg_prompt,
        num_inference_steps=int(steps),
        guidance_scale=float(scale),
        height=int(height),
        width=int(width),
    ).images[0]

    return image

# --- UI Layout ---
with gr.Blocks(title="PC Image Gen (OpenVINO)") as demo:
    gr.Markdown("# 🖥️ PC Personal Image Generator (4GB Optimized)")
    gr.Markdown(f"Running on: **AMD A4-9120C** via **OpenVINO**")

    with gr.Tabs():
        with gr.TabItem("Text-to-Image"):
            with gr.Row():
                with gr.Column():
                    prompt = gr.Textbox(
                        label="Prompt",
                        placeholder="Masterpiece, best quality, [subject]...",
                        lines=3
                    )
                    neg_prompt = gr.Textbox(
                        label="Negative Prompt",
                        value="low quality, blurry, deformed, bad anatomy",
                        lines=2
                    )
                    with gr.Row():
                        steps = gr.Slider(minimum=1, maximum=12, value=4, step=1, label="Steps (LCM: 4-8 recommended)")
                        scale = gr.Slider(minimum=1.0, maximum=4.0, value=1.0, step=0.1, label="Guidance Scale")
                    with gr.Row():
                        width = gr.Slider(minimum=256, maximum=512, value=512, step=64, label="Width")
                        height = gr.Slider(minimum=256, maximum=512, value=512, step=64, label="Height")
                    seed = gr.Number(label="Seed (-1 for random)", value=-1)
                    generate_btn = gr.Button("Generate", variant="primary")
                with gr.Column():
                    output_img = gr.Image(label="Generated Image")

            generate_btn.click(
                fn=generate,
                inputs=[prompt, neg_prompt, steps, scale, seed, height, width],
                outputs=output_img
            )

    gr.Markdown("---")
    gr.Markdown("### 💡 PC Optimization Tips:\n"
                "- **Steps**: Use **4 to 8 steps**. Since this is an LCM model, more steps won't always mean better quality.\n"
                "- **Resolution**: Stick to **512x512**. Higher resolutions will significantly increase memory usage.\n"
                "- **First Run**: The first generation will be slow because it has to compile the model for your CPU.")

if __name__ == "__main__":
    # share=False for local PC use, server_port 7861 to avoid conflict with S24 app
    demo.launch(server_name="0.0.0.0", server_port=7861)
