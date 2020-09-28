import cv2

def threshold_otsu():
 img=cv2.imread("Tile_004-003.jpg", 1)
 img2gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 ret,final_img=cv2.threshold(img2gray, 70, 150,
 cv2.THRESH_BINARY+cv2.THRESH_OTSU)
 cv2.imwrite('thresholded.jpg', final_img)

threshold_otsu()