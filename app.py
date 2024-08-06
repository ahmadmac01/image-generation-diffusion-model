import gradio as gr
import torch
from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("ahmadmac/images_Generation")

def generate_image(prompt, output_file="generated_image.png"):
  with torch.autocast("cpu"):  
    image = pipeline(prompt=prompt).images[0]
  image.save(output_file)
  return output_file

demo = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Prompt"),
    outputs=gr.Image(label="Generated Image")
)

demo.launch()
