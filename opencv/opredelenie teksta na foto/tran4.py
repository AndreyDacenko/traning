import cv2

def threshold_otsu():
 img=cv2.imread("Tile_005-004.jpg", 1)
 img2gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 ret,final_img=cv2.threshold(img2gray, 20, 150,
 cv2.THRESH_BINARY+cv2.THRESH_OTSU)
 cv2.imwrite('thresholded2.jpg', final_img)

threshold_otsu()