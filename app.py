import os
import torch
from diffusers import StableDiffusionPipeline, StableDiffusionInpaintPipeline
import gradio as gr
from PIL import Image
import numpy as np

# Configuration for 8GB RAM (S24 Standard)
MODEL_ID = "runwayml/stable-diffusion-v1-5" # Good baseline, can be swapped for NSFW models
DEVICE = "cpu" # Default for Termux, NPU acceleration requires specific drivers/libs
DTYPE = torch.float32 # CPU usually prefers float32

# Global variables for pipelines
txt2img_pipe = None
inpaint_pipe = None

def load_pipelines(model_path=MODEL_ID):
    global txt2img_pipe, inpaint_pipe
    
    print(f"Loading model: {model_path}...")
    
    # Text-to-Image Pipeline
    txt2img_pipe = StableDiffusionPipeline.from_pretrained(
        model_path, 
        torch_dtype=DTYPE,
        low_cpu_mem_usage=True,
        safety_checker=None, # Disabled for NSFW as requested
        requires_safety_checker=False
    ).to(DEVICE)
    
    # Memory Optimizations for 8GB RAM
    txt2img_pipe.enable_attention_slicing()
    
    # Inpainting Pipeline (Shared components to save RAM)
    inpaint_pipe = StableDiffusionInpaintPipeline(
        vae=txt2img_pipe.vae,
        text_encoder=txt2img_pipe.text_encoder,
        tokenizer=txt2img_pipe.tokenizer,
        unet=txt2img_pipe.unet,
        scheduler=txt2img_pipe.scheduler,
        safety_checker=None,
        feature_extractor=None,
        requires_safety_checker=False
    ).to(DEVICE)
    
    print("Models loaded successfully!")

def generate_txt2img(prompt, neg_prompt, steps, scale, seed, height, width):
    if txt2img_pipe is None:
        load_pipelines()
        
    generator = torch.Generator(DEVICE).manual_seed(int(seed)) if seed > -1 else None
    
    image = txt2img_pipe(
        prompt=prompt,
        negative_prompt=neg_prompt,
        num_inference_steps=int(steps),
        guidance_scale=scale,
        generator=generator,
        height=int(height),
        width=int(width)
    ).images[0]
    
    return image

def generate_inpaint(image_dict, prompt, neg_prompt, steps, scale, seed):
    if inpaint_pipe is None:
        load_pipelines()
        
    image = image_dict["background"].convert("RGB")
    mask = image_dict["layers"][0].convert("RGB") # Gradio Editor format
    
    generator = torch.Generator(DEVICE).manual_seed(int(seed)) if seed > -1 else None
    
    output = inpaint_pipe(
        prompt=prompt,
        negative_prompt=neg_prompt,
        image=image,
        mask_image=mask,
        num_inference_steps=int(steps),
        guidance_scale=scale,
        generator=generator
    ).images[0]
    
    return output

# --- UI Layout ---
with gr.Blocks(title="S24 Custom Image Gen") as demo:
    gr.Markdown("# 🚀 S24 Personal Image Generator (NSFW Enabled)")
    
    with gr.Tabs():
        # Tab 1: Text to Image
        with gr.TabItem("Text-to-Image"):
            with gr.Row():
                with gr.Column():
                    prompt = gr.Textbox(label="Prompt", placeholder="What do you want to see?", lines=3)
                    neg_prompt = gr.Textbox(label="Negative Prompt", placeholder="What to avoid...", lines=2)
                    with gr.Row():
                        steps = gr.Slider(minimum=1, maximum=50, value=20, step=1, label="Steps")
                        scale = gr.Slider(minimum=1, maximum=20, value=7.5, step=0.5, label="Guidance Scale")
                    with gr.Row():
                        width = gr.Slider(minimum=256, maximum=768, value=512, step=64, label="Width")
                        height = gr.Slider(minimum=256, maximum=768, value=512, step=64, label="Height")
                    seed = gr.Number(label="Seed (-1 for random)", value=-1)
                    generate_btn = gr.Button("Generate", variant="primary")
                with gr.Column():
                    output_img = gr.Image(label="Generated Image")
            
            generate_btn.click(
                fn=generate_txt2img,
                inputs=[prompt, neg_prompt, steps, scale, seed, height, width],
                outputs=output_img
            )

        # Tab 2: Inpainting
        with gr.TabItem("Inpainting (Edit)"):
            with gr.Row():
                with gr.Column():
                    input_img = gr.ImageMask(label="Upload Image & Paint Mask", type="pil")
                    inpaint_prompt = gr.Textbox(label="Prompt", placeholder="What to change/add?")
                    inpaint_btn = gr.Button("Inpaint", variant="primary")
                with gr.Column():
                    inpaint_output = gr.Image(label="Result")
            
            inpaint_btn.click(
                fn=generate_inpaint,
                inputs=[input_img, inpaint_prompt, neg_prompt, steps, scale, seed],
                outputs=inpaint_output
            )

    gr.Markdown("---")
    gr.Markdown("### 💡 Pro Tips for S24:\n"
                "- Use **Steps: 15-20** for a good balance of speed and quality.\n"
                "- Keep resolution at **512x512** for faster results on 8GB RAM.\n"
                "- For better NSFW results, download a specialized model (e.g., from Civitai) and swap the `MODEL_ID`.")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
