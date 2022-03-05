import cv2
import numpy as np
from pyzbar.pyzbar import decode
import pandas as pd
from datetime import date
import time
import pdf
import gui


cap = cv2.VideoCapture(0)
data = pd.read_csv('data.csv')
room_dict = {'Gastroenterology':1, 'Ear, Nose, Throat':2, 'Internal Medicine':3, 'Dermatology':4, 'Gynecology':5, 'Ophthalmoloy':6, 'Pediatrics':7, 'Orthopedics':8}


while True:
    success, img = cap.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (7, 7), 1)
    for qrcode in decode(blur_img):
        pin = qrcode.data.decode('utf8')
   
        points = np.array([qrcode.polygon], np.int32)
        cv2.polylines(img, [points], True, (0, 255, 0), 2)


        for i in range(0, len(data)):
            if pin == str(data['ID'][i]):
                name = data.loc[i]['Name']
                sex = data.loc[i]['Sex']
                dob = data.loc[i]['DOB']
                address = data.loc[i]['Address']
            
        
                birthdate = dob.split('/')
                print(birthdate)
                today = date.today()
                age = (today.year - int(birthdate[2])) - ((today.month, today.day) < (int(birthdate[0]), int(birthdate[1])))

                now = time.localtime()
                current_time = time.strftime("%H:%M:%S", now)

                gui.main()
                file = open("department.txt", "r")
                department = file.read()
                room_no = room_dict[department]

                pdf.main(pin, name, sex, age, address, today, current_time, department, room_no)

                filename = name + pin + '.jpg'
                cv2.imwrite(filename, img)
            else:
                print("Your data are not entered in the database. Please enter to use.")


    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break