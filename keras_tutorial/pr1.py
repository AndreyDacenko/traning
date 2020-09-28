
z = 0
if preds[0][1] > 0.95:

    z1 = preds[0][1]

    if z > z1:
        cv2.rectangle(img, (x, y), (x + 17, y + 94), (0, 255, 0), 1)
    else:
        z = z1

else:
    z = 0
