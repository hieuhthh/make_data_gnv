import os
import shutil

def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s'%(name,format), destination)

from_path = '/storage/hieunmt/make_gnv_face_dataset/gnv_dataset'
to_path = from_path + '.zip'
make_archive(from_path, to_path)