import cv2
import pandas as pd
import datetime
import numpy as np
#date=datetime.datetime.today().date()
date = input("Enter the date: ")
face_detect = cv2.CascadeClassifier("C:/Users/Asus/Downloads/haarcascade_frontalface_alt.xml")
cam = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("C:/Users/Asus/training.yml")
id = 0
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
df = pd.read_excel("C:/Users/Asus/Downloads/attendence2.xlsx")

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray, 2, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        id, conf = recognizer.predict(gray[x:x + w, y:y + h])
        Id1 = df['Name'][df.Id == id].iloc[0]  # Use .iloc[0] to get the actual value
        df.loc[df.Id == id, date] = 'P'  # Avoid SettingWithCopyWarning
        df.to_excel("C:/Users/Asus/Downloads/attendence2.xlsx", index=False)

        cv2.putText(frame, str(Id1), (x + w, y + h), font, 4, 255)

    cv2.imshow('frame', frame)
    w = cv2.waitKey(1)
    if w == 27:
        break

cam.release()
cv2.destroyAllWindows()