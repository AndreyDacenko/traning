import cv2
import numpy as np

if __name__ == '__main__':
    def nothing(*arg):
        pass

cv2.namedWindow("result")  # создаем главное окно
cv2.namedWindow("settings")  # создаем окно настроек

img = cv2.imread("Tile_005-004.jpg", 0)
# создаем 6 бегунков для настройки начального и конечного цвета фильтра
cv2.createTrackbar('h1', 'settings', 14, 255, nothing)
cv2.createTrackbar('s1', 'settings', 4, 25, nothing)
cv2.createTrackbar('v1', 'settings', 191, 255, nothing)
# cv2.createTrackbar('h2', 'settings', 0, 255, nothing)
# cv2.createTrackbar('s2', 'settings', 0, 255, nothing)
# cv2.createTrackbar('v2', 'settings', 0, 255, nothing)

while True:
    # считываем значения бегунков
    h1 = cv2.getTrackbarPos('h1', 'settings')
    if h1%2==0:
        h1 += 1
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    # h2 = cv2.getTrackbarPos('h2', 'settings')
    # s2 = cv2.getTrackbarPos('s2', 'settings')
    # v2 = cv2.getTrackbarPos('v2', 'settings')

    # накладываем фильтр на кадр в модели HSV
    _, th1 = cv2.threshold(img, v1, 255, cv2.THRESH_BINARY)
    blur = cv2.GaussianBlur(th1, (h1, h1), 0)
    ret3, th1 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # формируем начальный и конечный цвет фильтра
    # накладываем фильтр на кадр в модели HSV

    # images = [img, th1, th2, th3]
    kernel = np.ones((s1, s1), np.uint8)
    img_erosion = cv2.erode(th1, kernel, iterations=1)

    cv2.imshow('result', img_erosion)
    cv2.imwrite("thresholded6.jpg", img_erosion)
    ch = cv2.waitKey(5)
    if ch == 27:
        break

cv2.destroyAllWindows()
