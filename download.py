import gdown
import os
import shutil

des = 'download'

try:
    os.mkdir(des)
except:
    pass

# url = "https://drive.google.com/file/d/1s9PkpR3wkaKVnN4pxYcGjMBiJ0Q1F9Jx/view?usp=share_link"
# output =  f"{des}/data-active user-faceid-9112022.csv"
# gdown.download(url=url, output=output, quiet=False, fuzzy=True)

url = "https://drive.google.com/file/d/10QqMlQCGUxNQ5msHn0zSreaJaZLZSGci/view?usp=share_link"
output = f"{des}/saved_gallery.zip"
gdown.download(url=url, output=output, quiet=False, fuzzy=True)3