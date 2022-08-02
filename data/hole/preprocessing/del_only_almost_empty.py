import cv2
import numpy as np
import os
from pathlib import Path
from utilities import yield_imgs, delete_on_condition

enable_delete = True
threshold = 1100
# save_path = "../cropped_event_imgs"
# save_path = "../size_cropped_event_imgs"
save_path = "../grey_cropped_event_imgs"
# save_path = "../resized_imgs"

type_dir_list = os.listdir(save_path)

def is_almost_emty(img, threshold):
    # y, x, c = np.where(img != 255)
    y, x, c = np.where(img != 0)
    event_number = len(x) + len(y)

    if event_number <= threshold:
        return True

    return False


delete_on_condition(save_path, lambda x: is_almost_emty(x, threshold), enable_delete=enable_delete)  
