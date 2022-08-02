import cv2
import numpy as np

from utilities import yield_imgs, delete_on_condition


# path = "../resized_imgs"
path = "../maxpooled"
res = 256
size = 100

half_size = int(size / 2)

for img, file_path in yield_imgs(path):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    H, W = img.shape
    mid_x = int(res / 2)
    mid_y = int(res / 2)
    new_img = np.zeros((res,res))
    new_img[mid_y-half_size:mid_y+half_size, mid_x-half_size:mid_x+half_size] = img
 	
    


    # cv2.imshow("cropped", img)
    # cv2.waitKey(0)
    # break
    cv2.imwrite(file_path, new_img)