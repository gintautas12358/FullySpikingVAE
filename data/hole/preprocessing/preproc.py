
from crop_grey_images import crop_grey_img
from del_only_almost_empty import del_almost_empty
from del_only_out_of_bound import del_only_out_of_bound
from del_only_out_of_rec import del_only_out_of_rec
from resize_crop import resize_imgs
from maxpool import maxpool_img
from grey_background import grey_background
from grow import grow

save_path = "../preproc"
path = "../original_event_imgs"

size = 200
res = 256

threshold = 200

box_size = size
offset = 50

# offset = -12
# rec_size = 20

grow_size = 3

crop_grey_img(path, save_path, size)

del_almost_empty(save_path, threshold)

del_only_out_of_bound(save_path, box_size, offset)

resize_imgs(save_path, size, res)

for i in range(3):
    maxpool_img(save_path)

grow(save_path, grow_size)

grey_background(save_path)
