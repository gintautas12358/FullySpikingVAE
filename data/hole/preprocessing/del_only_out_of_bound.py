import cv2
import numpy as np
import os
from pathlib import Path
from utilities import yield_imgs, delete_on_condition

# enable_delete = True
offset = 50
# # save_path = "../cropped_event_imgs"
# save_path = "../grey_cropped_event_imgs"
save_path = "../preproc"
box_size = 200

def is_out_of_bound(img, box_size, offset):
    # positions_y, positions_x, channel = np.where(img != 255)
    positions_y, positions_x, channel = np.where(img != 0)

    min_position_x = np.min(positions_x)
    max_position_x = np.max(positions_x)
    min_position_y = np.min(positions_y)
    max_position_y = np.max(positions_y)

    mm = [min_position_x, max_position_x, min_position_y, max_position_y]

    is_out = False
    for m in mm:
        is_out |= 0 >= m - offset or box_size <= m + offset

    return is_out


# type_dir_list = os.listdir(save_path)
# print(type_dir_list)

# delete_on_condition(save_path, lambda x: is_out_of_bound(x, box_size, offset), enable_delete=enable_delete)

def del_only_out_of_bound(save_path, box_size, offset):
    type_dir_list = os.listdir(save_path)
    print(type_dir_list)

    delete_on_condition(save_path, lambda x: is_out_of_bound(x, box_size, offset), enable_delete=True)
    
# del_only_out_of_bound(save_path, box_size, offset)