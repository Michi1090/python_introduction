from PIL import Image

image = Image.open('flower.jpeg')
gray_image = image.convert('L')
gray_image.show()
gray_image.save('gray_image.jpeg')
