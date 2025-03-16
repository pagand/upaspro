from openai import OpenAI
import openai
import time
import base64
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# Assume the client already exists:
client = openai.OpenAI()

def encode_image_to_base64(image_path):
    """Reads an image file and converts it to a base64-encoded string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def describe_image(model, image, prompt):
    """Sends a base64-encoded image to OpenAI's vision model and gets a description."""
    if image.get("URL", None):
        image_url = image["URL"]
        content = image_url
    elif image.get("path", None):
        image_path = image["path"]
        image_data = encode_image_to_base64(image_path)
        content = f"data:image/jpeg;base64,{image_data}"
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"{prompt}"},
                    {"type": "image_url", "image_url":{ "url": content}}
                ]
            }
        ],
        max_tokens=200,
        temperature=0.5,
    )
    
    return response.choices[0].message.content

# Example usage
model = "gpt-4o-mini"
image_url = "https://www.communitycatspodcast.com/wp-content/uploads/2023/03/Cat6.jpg"
image_path = "./image.jpg"  # Replace with your local image path
description_1 = describe_image(model, {"path": image_path}, "Describe this image:")
description_2 = describe_image(model, {"URL": image_url}, "Describe this image:")
print("Local:", description_1)
print("URL:", description_2)
