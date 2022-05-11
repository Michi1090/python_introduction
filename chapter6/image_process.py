from lib2to3.pytree import convert
from PIL import Image

image = Image.open('flower.jpeg')
red, green, blue = image.split()
convert_image = Image.merge('RGB', (blue, green, red))
convert_image.show()
convert_image.save('rgb_to_bgr.jpeg')
