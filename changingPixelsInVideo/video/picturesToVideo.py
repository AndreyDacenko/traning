import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('capturesChanged/*.jpg'):
    img = cv2.imread(filename)
    size = (1280, 720)
    img_array.append(img)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 60, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
