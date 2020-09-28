import cv2
vidcap = cv2.VideoCapture("video.mp4")
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  # cv2.imwrite("captures/frame%d.jpg" % count, image)     # save frame as JPEG file
  cv2.imwrite(f"captures/frame{count:06d}.jpg", image)  # save frame as JPEG file
  count += 1