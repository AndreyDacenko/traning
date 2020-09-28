import numpy
import cv2
from keras.models import load_model
import argparse
import pickle

m = "output\\simple_nn.model"
l_b = "output\\simple_nn_lb.pickle"

img = cv2.imread("MEDIUM.jpg")

x = 0
y = 4
maxWidth = img.shape[1]
maxHeight = img.shape[0]

print("[INFO] loading network and label binarizer...")
model = load_model(m)
lb = pickle.loads(open(l_b, "rb").read())
# z = 0


map = numpy.zeros((maxHeight,maxWidth))

def crop(x, y):
    # global z
    global map
    crop_img = img[y:94 + y, x:17 + x]
    im = cv2.resize(crop_img, (64, 64))
    im = im.astype("float") / 255.0
    im = im.reshape((1, im.shape[0], im.shape[1],
                           im.shape[2]))
    preds = model.predict(im)
    print(preds)

    if preds[0][1] > 0.97:
        cv2.rectangle(img, (x, y), (x + 17, y + 94), (0, 255, 0), 1)

        map[y][x] = preds[0][1]
        # map.append(preds[0][1])
    # else:
    #      map.append(0)

    # if preds[0][1] > 0.9:
    #     z1 = preds[0][1]
    #     if z > z1:
    #         cv2.rectangle(img, (x, y), (x + 17, y + 94), (0, 255, 0), 1)
    #         z = 0
    #     else:
    #         z = z1

while y < (maxHeight - 94):
    x = 0
    while x < (maxWidth - 17):
        crop(x, y)
        x += 1
    y += 93

# print(map)
cv2.imshow("map", map)
cv2.imwrite("map.jpg", map * 255)
cv2.imwrite("result.jpg", img)
cv2.imshow("result", img)
cv2.waitKey(0)

