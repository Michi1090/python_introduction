from PIL import Image

image = Image.open('flower.jpeg')
black_and_white = image.convert('1')
black_and_white.show()
black_and_white.save('b_and_w.jpeg')
