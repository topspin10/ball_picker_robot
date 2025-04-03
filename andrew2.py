from PIL import Image, ImageDraw, ImageFont

# Create a blank white image
img = Image.new('RGB', (200, 100), color=(255, 255, 255))

# Initialize ImageDraw object to draw on the image
draw = ImageDraw.Draw(img)

# Use the default font (you can change the font if needed)
font = ImageFont.load_default()

# Positioning the numbers on the image
draw.text((10, 10), "0", fill=(0, 0, 0), font=font)
draw.text((50, 10), "1", fill=(0, 0, 0), font=font)
draw.text((90, 10), "2", fill=(0, 0, 0), font=font)

# Save the image with the numbers
img.save('image_with_numbers.png')

# Optionally, show the image
img.show()
