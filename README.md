# Image Generator
This project leverages the power of the diffusers library and the gradio interface to generate images based on text prompts. The model used is fine-tuned on stray cat images, enabling the generation of high-quality images of stray cats based on user input.

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
The code defines a simple web interface where users can input a text prompt to generate an image of a stray cat.
## Import libraries
```python
import gradio as gr
import torch
from diffusers import DiffusionPipeline
```
## Load pipeline
```python
pipeline = DiffusionPipeline.from_pretrained("ahmadmac/stray-cat")
```
## Model
The model used in this project is fine-tuned on images of stray cats. It is capable of generating realistic and detailed images of stray cats based on descriptive text prompts.
[Model link](https://huggingface.co/ahmadmac/stray-cat)

## Example
To generate an image of a stray cat, enter a prompt such as "A stray cat sitting on a sidewalk" and click the "Generate Image" button. The generated image will be displayed in the interface.
## [Hugging Face Space Link](https://huggingface.co/spaces/ahmadmac/stray-cat-image-generation)

