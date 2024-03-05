import openai

# Initialize the OpenAI client
client = openai.OpenAI()

# Edit an image using DALL-E based on a textual prompt and a mask
response = client.images.edit(
    model="dall-e-2",  # Specify the model version to use for the image editing
    size="512x512",  # Define the resolution of the output image
    image=open("living-room.png", "rb"),  # Open the source image file in binary mode
    mask=open("living-room-mask.png", "rb"),  # Open the mask image file in binary mode
    prompt="An image of a minimalist living room featuring a large, comfortable looking, two-person couch in the center. The room has plain walls and a simple, polished wooden floor. There is ample natural light coming in from a large window, creating a bright and open space. The overall look is clean, uncluttered, and modern.",  # Textual description to guide the editing process
)

# Extract the URL of the edited image from the response
image_url = response.data[0].url
# Print the URL of the edited image to the console
print(image_url)
