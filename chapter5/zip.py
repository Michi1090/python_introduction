import zipfile

files = zipfile.ZipFile('normal_typhoon.zip')
files.namelist()
files.extract('normal_typhoon/nml_typhoon.pdf')
files.extractall()
files.close


zip_file = zipfile.ZipFile('プロフィール画像.zip', mode = 'w')
zip_file.write('プロフィール画像.JPG')
zip_file.close()
file = zipfile.ZipFile('プロフィール画像.zip')
file.namelist()
