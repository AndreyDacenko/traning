import cv2


def treshold():
 test_img=cv2.imread('Tile_005-004.jpg')
 img2gray=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
 ret,final_img=cv2.threshold(img2gray,170,220,cv2.THRESH_BINARY)
 cv2.imwrite('thresholded2.jpg', final_img)
 # cv2.imshow('Thresholding', final_img)
 #
 # cv2.waitKey()
 # cv2.destroyAllWindows()

treshold()
