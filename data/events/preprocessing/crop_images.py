import cv2
import numpy as np
import os
from pathlib import Path

save_path = "../cropped_event_imgs"
path = "../original_event_imgs"

size = 64


def center_crop(img, size):
    half_size = int(size / 2)

    positions_y, positions_x, channel = np.where(img > 0)
    min_position_x = np.min(positions_x)
    max_position_x = np.max(positions_x)
    min_position_y = np.min(positions_y)
    max_position_y = np.max(positions_y)

    mid_x = int((min_position_x + max_position_x) / 2)
    mid_y = int((min_position_y + max_position_y) / 2)

    # print(min_position_x, max_position_x, min_position_y, max_position_y)

    crop_img = img[mid_y-half_size:mid_y+half_size, mid_x-half_size:mid_x+half_size]
    return crop_img


type_dir_list = os.listdir(path)

print(type_dir_list)

for type in type_dir_list:
    print(type)
    type_path = os.path.join(path, type)
    type_save_path = os.path.join(save_path, type)

    Path(type_save_path).mkdir(parents=True, exist_ok=True)

    dir_list = os.listdir(type_path)

    for f in dir_list:
        file_path = os.path.join(type_path, f)
        img = cv2.imread(file_path)

        # crop_img = img[y:y+size, x:x+size]
        crop_img = center_crop(img, size)


        # for visibility
        crop_img = np.where(crop_img == 0, 255, crop_img)

        new_img_path = os.path.join(type_save_path, f)
        cv2.imwrite(new_img_path, crop_img)

print("Done!\n")