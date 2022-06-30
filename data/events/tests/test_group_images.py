import cv2
import numpy as np
import os
from pathlib import Path

save_path = "../grouped_event_imgs"


def get_file_number(f):
    name = f.split(".")[0]
    number = int(name)
    return number


def is_not_in_sequence(lis):
    step = 2

    if len(lis) < 2:
        return True

    not_in_sequence = False
    last_number = get_file_number(lis[0])
    for f in lis[1:]:
        number = get_file_number(f)
        diff = number - last_number 
        not_in_sequence |= diff != 2
        last_number = number

    return not_in_sequence

type_dir_list = os.listdir(save_path)

print(type_dir_list)

for type in type_dir_list:
    print(type)
    type_path = os.path.join(save_path, type)
    type_save_path = os.path.join(save_path, type)

    dir_list = os.listdir(type_path)
    dir_list.sort()
    
    for group in dir_list:
        
        group_type_save_path = os.path.join(type_path, group)
        file_list = os.listdir(group_type_save_path)

        file_list.sort()

        if is_not_in_sequence(file_list):
            print(group)
            print(file_list)
            print("found error")

        if len(file_list) < 16:
            print(group)
            print(file_list)
            print("not enough")

print("Done!\n")