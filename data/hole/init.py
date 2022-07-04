import os

file_name = "data_info.txt"
path = "small_grey_cropped_event_imgs"
# path = "grey_cropped_event_imgs"
# path = "cropped_event_imgs"

splits = {
    "train": 0.8,
    "test": 0.2,
}

def dataset_size(path, type_list):

    sizes = {}
    for type_folder in type_list:
        path_folder = os.path.join(path, type_folder)
        lis = os.listdir(path_folder)
        sizes[type_folder] = len(lis)

    return sizes

# emty file
with open(file_name, "w") as f:
    f.write("")

type_list = os.listdir(path)
type_list.sort()

sizes = dataset_size(path, type_list)
train_sizes = {}
test_sizes = {}
for k, v in sizes.items():
    train_sizes[k] = int(v * splits["train"])
    test_sizes[k] = v  - train_sizes[k]

train_size = 0
for size in train_sizes.values():
    train_size += size

test_size = 0
for size in test_sizes.values():
    test_size += size
    
with open(file_name, "a") as f:
    f.write(f"{train_size} {test_size}  {1} {train_size + 2}\n")

test_set = []
counter = 0
for type_folder in type_list:
    path_folder = os.path.join(path, type_folder)

    file_list = os.listdir(path_folder)
    file_list.sort()

    for i in range(train_sizes[type_folder]):
        file = file_list[i]
        path_file = os.path.join(type_folder, file)

        # write info
        with open(file_name, "a") as f:
            f.write(f"{path_file} {counter}\n")

        counter += 1

    for i in range(train_sizes[type_folder], train_sizes[type_folder] + test_sizes[type_folder]):
        file = file_list[i]
        path_file = os.path.join(type_folder, file)
        test_set.append(path_file)

with open(file_name, "a") as f:
        f.write("############### test ###############\n")

counter = 0
for path_file in test_set:
    # write info
    with open(file_name, "a") as f:
        f.write(f"{path_file} {counter}\n")

    counter += 1