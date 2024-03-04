from openai import OpenAI

client = OpenAI(organization='org-ZVWK5vUq8qs3kUsZVCMvNUgR')

response = client.images.generate(
    model="dall-e-3",
    prompt="A serene lake surrounded by autumn trees",
    size="1024x1024",
    style="vivid",
    quality="standard",
    response_format="url",
    n=1,
)

image_url = response.data[0].url
print(image_url)