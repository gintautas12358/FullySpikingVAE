import cv2
import numpy as np
import os
from pathlib import Path
from utilities import yield_imgs, delete_on_condition

enable_delete = True
offset = 5
# save_path = "../cropped_event_imgs"
save_path = "../grey_cropped_event_imgs"

def is_out_of_bound(img, offset):
    # positions_y, positions_x, channel = np.where(img != 255)
    positions_y, positions_x, channel = np.where(img != 0)

    min_position_x = np.min(positions_x)
    max_position_x = np.max(positions_x)
    min_position_y = np.min(positions_y)
    max_position_y = np.max(positions_y)

    mm = [min_position_x, max_position_x, min_position_y, max_position_y]

    is_out = False
    for m in mm:
        is_out |= 0 >= m - offset or 64 <= m + offset

    if is_out:
        return True

    return False


type_dir_list = os.listdir(save_path)
print(type_dir_list)

delete_on_condition(save_path, lambda x: is_out_of_bound(x, offset), enable_delete=enable_delete)
    
