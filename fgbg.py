import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#fgbg = cv2.createBackgroundSubtractorMOG2()


while(1):
    ret, frame = cap.read()
    #fgmask = fgbg.apply(frame)
    cv2.imshow('orignal', frame)
    #cv2.imshow('fg', fgmask)

    if cv2.waitKey(0):
        break
    #k = cv2.waitKey(30) & 0xff
    #if k == 27:
    #    break
cap.release()
cv2.destroyAllWindows()
