import cv2
import numpy as np

from utilities import yield_imgs, delete_on_condition

# path = "../small_grey_cropped_event_imgs"
# path = "../resized_imgs"
# path = "../maxpooled"
# path = "../dilated"


# for img, file_path in yield_imgs(path):
    
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img = np.where(img == 0, 127, img)
#     img = np.where(img == 129, 0, img)
    

#     cv2.imwrite(file_path, img)

def grey_background(path):
    for img, file_path in yield_imgs(path):
    
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.where(img == 0, 127, img)
        img = np.where(img == 129, 0, img)
        

        cv2.imwrite(file_path, img)