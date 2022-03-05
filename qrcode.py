import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    for qrcode in decode(img):
        pin = qrcode.data.decode('utf8')
        print(pin)
        
        points = np.array([qrcode.polygon], np.int32)
        print(points)
        cv2.polylines(img, [points], True, (0, 255, 0), 2)

        

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break