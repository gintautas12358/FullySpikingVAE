import os 
import re

enable_delete = False

def extract_int(s):
    x = re.findall('[0-9]+', s)
    return int(x[0])

runs_list = os.listdir()
exclude = 'reduce_imgs.py'

print(runs_list)


paths_to_reduce = {"sample": 1, "test": 2, "train": 2}

# run = runs_list[6]

for run in runs_list:
    if run == exclude:
        continue
    
    print(run)
    for path in paths_to_reduce:
        base_path = run + "/imgs/"

        if "imgs" not in os.listdir(run):
            continue

        if path not in os.listdir(run + "/imgs"):
            continue

        images_list = os.listdir(base_path + path)

        images_list.sort(key=extract_int)

        # for i in images_list[:5]:
        #     print(i)

        size = len(images_list)
        print(run, path, size)

        # print("last are:")
        # for i in range(0,paths_to_reduce[path]):
        #     print(images_list[size-i-1])
        
        for f in images_list[:size-2]:
            file_path = base_path + path + "/" + f
            if enable_delete:
                os.remove(file_path)

