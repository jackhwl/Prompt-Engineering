from openai import OpenAI
import base64

client = OpenAI(organization='org-ZVWK5vUq8qs3kUsZVCMvNUgR')

response = client.images.generate(
    model="dall-e-3",
    prompt="A serene lake surrounded by autumn trees",
    size="1024x1024",
    style="vivid",
    quality="standard",
    response_format="b64_json",
    n=1,
)

image_b64 = response.data[0].b64_json

image_data = base64.b64decode(image_b64)

with open("downloaded_image.png", "wb") as image_file:
    image_file.write(image_data)

print("Image saved successfully.")