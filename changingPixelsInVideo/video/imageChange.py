import cv2
import numpy as np
import glob

# img_array = []
img_names = []
for filename in glob.glob('./captures/*.jpg'):
    # img_array.append(cv2.imread(filename, 0))
    # print(filename.split("\\")[1])
    img_names.append(filename)


print(img_names)

for image_name in img_names:
    image = cv2.imread(image_name, 1)
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            # print(image[y][x])
            if (x + y) % 4 == 0:
                image[y][x] = [0, 0, 255]
                # print(image[y][x])
    name = image_name.split('\\')[1]
    #cv2.imwrite(f"capturesChanged/{name}.jpg", image)  # save frame as JPEG file
    cv2.imwrite("capturesChanged/{0}.jpg".format(name), image)  # save frame as JPEG file

