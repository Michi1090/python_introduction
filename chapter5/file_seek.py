from unittest import result


file_object = open('python.txt', 'r+')
result = file_object.read()
file_object.write('Happy Hacking!')
file_object.seek(0)
file_object.read()
file_object.close()
