# Import Image and ImageDraw
from PIL import Image, ImageDraw
# Create black image
img = Image.new("RGB", (100,100))
# Create draw obeject
draw = ImageDraw.Draw(img)
# Place a point on the image
draw.point((50,50),)
# Show the image
img.show()
