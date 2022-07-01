import os

file_name = "data_info.txt"
path = "grey_cropped_event_imgs"
# path = "cropped_event_imgs"


# emty file
with open(file_name, "w") as f:
    f.write("")

type_list = os.listdir(path)
type_list.sort()

counter = 0
for type_folder in type_list:
    path_folder = os.path.join(path, type_folder)

    file_list = os.listdir(path_folder)
    file_list.sort()

    for file in file_list:

        path_file = os.path.join(type_folder, file)

        # write info
        with open(file_name, "a") as f:
            f.write(f"{path_file} {counter}\n")

        counter += 1
