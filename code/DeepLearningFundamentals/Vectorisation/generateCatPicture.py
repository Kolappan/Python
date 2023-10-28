from PIL import Image

# Create a new image with RGB mode
image = Image.new('RGB', (8, 8))

# Define your pixel values (for a basic example)
pixel_values = [
    (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0),
    (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0),
    (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0),
    (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0),
    (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0),
    (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0)
]

# Set the pixel values in the image
image.putdata(pixel_values)

# Save the image
image.save("cat_image.png")
