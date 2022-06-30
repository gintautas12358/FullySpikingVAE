import numpy as np
import os
from utilities import yield_imgs, delete_on_condition

enable_delete = True
save_path = "../cropped_event_imgs"

def is_white(img):
    return np.all(img == 255)


delete_on_condition(save_path, is_white, enable_delete=enable_delete)

    
