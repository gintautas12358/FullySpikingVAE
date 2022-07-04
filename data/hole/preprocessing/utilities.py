import cv2
import numpy as np
import os
from pathlib import Path


def yield_imgs(path):
    type_dir_list = os.listdir(path)

    print(type_dir_list)

    for type in type_dir_list:
        print(type)
        type_save_path = os.path.join(path, type)

        Path(type_save_path).mkdir(parents=True, exist_ok=True)

        dir_list = os.listdir(type_save_path)

        for f in dir_list:
            file_path = os.path.join(type_save_path, f)
            img = cv2.imread(file_path)

            yield img, file_path

    print("Done!\n")

def delete_on_condition(path, condition, enable_delete=False):
    for img, file_path in yield_imgs(path):
        if condition(img):
            print(file_path)
            if enable_delete:
                os.remove(file_path)
