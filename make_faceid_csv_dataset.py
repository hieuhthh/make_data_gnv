from PIL import Image
import requests
from io import BytesIO
import numpy as np
import pandas as pd
import os
import cv2
import gdown
import shutil

from crop_face import *

df_path = 'download/data-active user-faceid-9112022.csv' 
df = pd.read_csv(df_path, encoding='ISO-8859-1')

route = 'gnv'

try:
    os.mkdir(route)
except:
    pass

def url2img(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        img = Image.open(BytesIO(response.content)) # already rgb
        img = np.array(img)
        return img
    except:
        return None

def create_face_stage(stage):
    route_stage = f"{route}/{stage}"

    try:
        os.mkdir(route_stage)
    except:
        pass

    cnt = 0
    for index, row in df.iterrows():
        domain = row['domain']
        domain_path = route_stage + '/' + domain
        try:
            os.mkdir(domain_path)
        except:
            pass

        url_face = row[stage]
        img = url2img(url_face)

        if img is None:
            print('Face is None:', domain, stage)
            continue
        
        img = img[...,::-1] # rgb2bgr
        bb_box = extract_face(img)
        
        try:
            img = crop_face(img, bb_box)

            if img is None:
                continue

            cv2.imwrite(f'{domain_path}/{domain}_{cnt}.jpg', img)
            cnt += 1
        except:
            print('BBox is None:', domain, stage)

    print("Count", stage, cnt)

stage = 'frontal_face'
create_face_stage(stage)

stage = 'masked_face'
create_face_stage(stage)

stage = 'skewed_face'
create_face_stage(stage)