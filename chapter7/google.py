import qrcode

encode_text = 'https://google.com'
img = qrcode.make(encode_text)
print(type(img))
img.show()
