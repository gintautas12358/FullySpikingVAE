import cv2
import numpy as np

file_path = "../original_event_imgs/usb/00000067.png"
img = cv2.imread(file_path)

size = 300
half_size = int(size / 2)
# x = 600
# y = 430

positions_y, positions_x, channel = np.where(img > 0)
min_position_x = np.min(positions_x)
max_position_x = np.max(positions_x)
min_position_y = np.min(positions_y)
max_position_y = np.max(positions_y)

mid_x = int((min_position_x + max_position_x) / 2)
mid_y = int((min_position_y + max_position_y) / 2)

print(min_position_x, max_position_x, min_position_y, max_position_y)

H, W, C = img.shape

# crop_img = img[mid_y-half_size:mid_y+half_size, mid_x-half_size:mid_x+half_size]
crop_img = img[H - size:H, mid_x-half_size:mid_x+half_size]
# crop_img = img

crop_img = np.where(crop_img == 0, 255, crop_img)
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)