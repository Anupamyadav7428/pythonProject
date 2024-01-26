import pandas as pd
import cv2

# Read Excel file into a DataFrame
df = pd.read_excel("C:/Users/Asus/Downloads/attendence2.xlsx")

# Initialize face cascade classifier and video capture
face_cascade = cv2.CascadeClassifier("C:/Users/Asus/Downloads/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

# Input ID and Name, update DataFrame, and save to Excel
Id = input("Enter the ID: ")
Name = input("Enter the Name: ")
df2 = pd.DataFrame({'Id': [Id], 'Name': [Name]})
df = pd.concat([df, df2]).drop_duplicates().reset_index(drop=True)
df.to_excel("C:/Users/Asus/Downloads/attendence2.xlsx", index=False)

sampleNum = 0

while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))
        sampleNum = sampleNum + 1
        cv2.imwrite(f"C:/Users/Asus/image detect/user.{Id}.{sampleNum}.jpg", frame[y:y+h, x:x+w])
        cv2.imshow('frame', frame)

    w = cv2.waitKey(100)

    if w == 27:
        break
    elif sampleNum > 10:
        break

cap.release()
cv2.destroyAllWindows()
