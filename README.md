# Image Generator
This project uses a fine-tuned diffusion model to generate images based on textual prompts. The model has been fine-tuned on my 250  images to produce more relevant and personalized results. The image generation process is managed using the diffusers library, and a user interface is built with Gradio.

## Installation
1. To run this project, you will need to install the required Python libraries. You can do this using pip:
```python
   !pip install gradio torch diffusers
```
2. To install requirements.txt file
```python
    !pip insatall -r requirements.txt
```
## Usage
The code defines a simple web interface where users can input a text prompt to generate an image.
## Import libraries
```python
import gradio as gr
import torch
from diffusers import DiffusionPipeline
```
## Load pipeline
```python
pipeline = DiffusionPipeline.from_pretrained("ahmadmac/images_Generation")
```
## Model
The model used for image generation has been fine-tuned on 250 images. This fine-tuning process enhances the model's ability to generate images that are more aligned with specific needs and preferences based on the provided prompts.
[Model link](https://huggingface.co/ahmadmac/Images_Generation)

## Example
To generate an image, enter a prompt and click the "Generate Image" button. The generated image will be displayed in the interface.
## [Hugging Face Space Link](https://huggingface.co/spaces/ahmadmac/Images_Generator)

