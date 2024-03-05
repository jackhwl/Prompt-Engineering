import openai

# Initialize the OpenAI client for API access
client = openai.OpenAI()

# Request to generate variations of an existing image using DALL-E
response = client.images.create_variation(
    model="dall-e-2",  # Specify the model version to use for generating variations
    image=open("owl.png", "rb"),  # Open and read the original image file in binary mode
    n=3,  # Specify the number of image variations to generate
    size="1024x1024",  # Define the resolution of the generated image variations
)

# Iterate through the generated image variations
for image in response.data:
    image_url = image.url  # Extract the URL of the generated image variation
    print(image_url)  # Print the URL to the console
