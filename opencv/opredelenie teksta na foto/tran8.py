import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    def nothing(*arg):
        pass

cv2.namedWindow("result")  # создаем главное окно
cv2.namedWindow("settings")  # создаем окно настроек

img=cv2.imread("Tile_005-004.jpg", 1)
# создаем 6 бегунков для настройки начального и конечного цвета фильтра
cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
cv2.createTrackbar('v2', 'settings', 170, 255, nothing)

crange = [0, 0]

while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # считываем значения бегунков
    v1 = cv2.getTrackbarPos('v1', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')


    # формируем начальный и конечный цвет фильтра
    h_min = np.array((v1), np.uint8)
    h_max = np.array((v2), np.uint8)

    # накладываем фильтр на кадр в модели HSV
    thresh = cv2.inRange(hsv, h_min, h_max)

    cv2.imshow('result', thresh)

    ch = cv2.waitKey(5)
    if ch == 27:
        break



cv2.imwrite('thresholded3.jpg', thresh)
img.release()
cv2.destroyAllWindows()