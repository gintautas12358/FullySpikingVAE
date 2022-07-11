import cv2
import numpy as np

from utilities import yield_imgs, delete_on_condition


path = "../size_cropped_event_imgs"
res = 300


half_size = int(res / 2)

for img, file_path in yield_imgs(path):
    
    H, W, _ = img.shape
    mid_x = int(W / 2)
    crop_img = img[H - res:H, mid_x-half_size:mid_x+half_size]

    crop_img = np.where(crop_img == 50, 255, crop_img)

        	
    crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    max_value = np.max(crop_img)
    crop_img = cv2.normalize(crop_img,  crop_img, 0, 255, cv2.NORM_MINMAX)

    # cv2.imshow("cropped", img)
    # cv2.waitKey(0)
    # break
    cv2.imwrite(file_path, crop_img)