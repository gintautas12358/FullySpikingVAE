import cv2
import numpy as np
import os
from pathlib import Path

# save_path = "../grey_cropped_event_imgs"
# path = "../original_event_imgs"
# path = "../grey_cropped_event_imgs"

size = 20


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


# type_dir_list = os.listdir(path)

# print(type_dir_list)

# for type in type_dir_list:
#     print(type)
#     type_path = os.path.join(path, type)
#     type_save_path = os.path.join(save_path, type)

#     Path(type_save_path).mkdir(parents=True, exist_ok=True)

#     dir_list = os.listdir(type_path)

#     for f in dir_list:
#         file_path = os.path.join(type_path, f)
#         # print(file_path)
#         img = cv2.imread(file_path)

#         # crop_img = img[y:y+size, x:x+size]
#         crop_img = center_crop(img, size)

#         if crop_img.shape[0] < size or crop_img.shape[1] < size:
#             continue

#         # for visibility
#         crop_img = np.where(crop_img == 50, 255, crop_img)
#         if crop_img[0].size == 0 or crop_img[1].size == 0:
#             continue
        	
#         crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

#         max_value = np.max(crop_img)
#         crop_img = cv2.normalize(crop_img,  crop_img, 0, 255, cv2.NORM_MINMAX)

#         new_img_path = os.path.join(type_save_path, f)
#         cv2.imwrite(new_img_path, crop_img)

# print("Done!\n")


def crop_grey_img(path, save_path, size):
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
            # print(file_path)
            img = cv2.imread(file_path)

            if img is None:
                continue

            # crop_img = img[y:y+size, x:x+size]
            crop_img = center_crop(img, size)

            if crop_img.shape[0] < size or crop_img.shape[1] < size:
                continue

            # for visibility
            crop_img = np.where(crop_img == 50, 255, crop_img)
            if crop_img[0].size == 0 or crop_img[1].size == 0:
                continue
                
            crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

            max_value = np.max(crop_img)
            crop_img = cv2.normalize(crop_img,  crop_img, 0, 255, cv2.NORM_MINMAX)

            new_img_path = os.path.join(type_save_path, f)
            cv2.imwrite(new_img_path, crop_img)

    print("Done!\n")