import cv2
import numpy as np
import os
from pathlib import Path
from utilities import yield_imgs, delete_on_condition

# enable_delete = True
offset = -100
rec_size = 200
# save_path = "../cropped_event_imgs"
# save_path = "../grey_cropped_event_imgs"
save_path = "../preproc"


def is_out_of_rec(img, rec_size, offset):
    # positions_y, positions_x, channel = np.where(img != 255)
    positions_y, positions_x, channel = np.where(img != 0)

    if positions_x.size == 0:
        return True

    min_position_x = np.min(positions_x)
    max_position_x = np.max(positions_x)
    min_position_y = np.min(positions_y)
    max_position_y = np.max(positions_y)

    if max_position_x - min_position_x > rec_size + offset or max_position_y - min_position_y > rec_size + offset:
        return True

    return False


# type_dir_list = os.listdir(save_path)
# print(type_dir_list)


# delete_on_condition(save_path, lambda x: is_out_of_rec(x, offset), enable_delete=enable_delete)

def del_only_out_of_rec(save_path, rec_size, offset):
    type_dir_list = os.listdir(save_path)
    print(type_dir_list)
    delete_on_condition(save_path, lambda x: is_out_of_rec(x, rec_size, offset), enable_delete=True)

# del_only_out_of_rec(save_path, rec_size, offset)