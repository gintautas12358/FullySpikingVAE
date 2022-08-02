import cv2
import numpy as np

import numpy as np
import skimage.measure

from utilities import yield_imgs, delete_on_condition

# path = "../small_grey_cropped_event_imgs"
# path = "../resized_imgs"
path = "../maxpooled"


for img, file_path in yield_imgs(path):
    
    # print(img.shape)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = skimage.measure.block_reduce(img, (2,2), np.max)
    

    cv2.imwrite(file_path, img)