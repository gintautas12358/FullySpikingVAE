import cv2
import numpy as np

from utilities import yield_imgs, delete_on_condition

# path = "../small_grey_cropped_event_imgs"
# path = "../resized_imgs"
# path = "../maxpooled"
# path = "../dilated"



# size = 5

# for img, file_path in yield_imgs(path):
    
#     kernel = np.ones((size,size), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     cv2.imwrite(file_path, img)


def grow(path, size):
    for img, file_path in yield_imgs(path):
    
        kernel = np.ones((size,size), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(file_path, img)