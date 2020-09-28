
import cv2


def edges_canny():
 img=cv2.imread("thresholded3.jpg", 1)
 img2gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 edges = cv2.Canny(img2gray,50,50)
 cv2.imshow('edges', edges)
 cv2.imwrite('thresholded4.jpg', edges)
edges_canny()

cv2.waitKey()
cv2.destroyAllWindows()