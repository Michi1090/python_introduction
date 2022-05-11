from PIL import Image

image = Image.open('flower.jpeg')
image.transpose(Image.ROTATE_90).show()
image.transpose(Image.ROTATE_90).save('rotate_90.jpeg')
