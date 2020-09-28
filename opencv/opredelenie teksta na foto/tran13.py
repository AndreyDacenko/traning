import scipy
from scipy import ndimage

im = scipy.misc.imread('thresholded4.jpg',flatten=1)
#threshold image, so its binary, then invert (`label` needs this):
im[im>100]=255
im[im<=100]=0
im = 255 - im
#label the image:
blobs, number_of_blobs = ndimage.label(im)
#remove all labelled blobs that are outside of our size constraints:
for i in range(number_of_blobs):
    if blobs[blobs==i].size < 40 or blobs[blobs==i].size>150:
im[blobs==i] = 0
scipy.misc.imsave('out.jpg', im)