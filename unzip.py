import zipfile
import os
import shutil

from_dir = 'download'
des = 'unzip'
try:
    os.mkdir(des)
except:
    pass

filename = 'saved_gallery'
zip_file = os.path.join(from_dir, filename + '.zip')
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(des)