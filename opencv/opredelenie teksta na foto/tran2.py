import cv2



def edges_canny():
 img=cv2.imread("Tile_004-003.jpg", 1)
 img2gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 edges = cv2.Canny(img2gray,140,255)
 cv2.imwrite('thresholded.jpg', edges)

edges_canny()