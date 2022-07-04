import cv2
import numpy as np
import os
from pathlib import Path

save_path = "../grouped_event_imgs"
path = "../cropped_event_imgs"

def get_file_number(f):
    name = f.split(".")[0]
    number = int(name)
    return number


def is_not_in_sequence(f1, f2):
    step = 2

    last_number = get_file_number(f1)
    number = get_file_number(f2)
    diff = number - last_number 

    return diff != step


def create_group(file_dic, group_type_save_path):
    print(group_type_save_path, len(file_dic))
    Path(group_type_save_path).mkdir(parents=True, exist_ok=True)
    for k, v in file_dic.items():
        cv2.imwrite(os.path.join(group_type_save_path, k), v)

def create_file_groups(dir_list):
    group_counter = 0
    file_counter = 0
    file_dic = {}

    last_f = dir_list[0]
    for f in dir_list[1:]:
        # read it from the input folder
        file_path = os.path.join(type_path, f)
        img = cv2.imread(file_path)

        if is_not_in_sequence(last_f, f):
            file_dic = {}
            file_counter = 0

        # remember for writing
        file_dic[f] = img
        file_counter += 1

        last_f = f

        if file_counter == 16:
            group_type_save_path = os.path.join(type_save_path, str(group_counter))
            create_group(file_dic, group_type_save_path)

            # reset
            file_dic = {}
            file_counter = 0

            group_counter += 1


type_dir_list = os.listdir(path)

print(type_dir_list)

for type in type_dir_list:
    print(type)
    type_path = os.path.join(path, type)
    type_save_path = os.path.join(save_path, type)

    Path(type_save_path).mkdir(parents=True, exist_ok=True)

    dir_list = os.listdir(type_path)
    dir_list.sort()

    create_file_groups(dir_list)

print("Done!\n")