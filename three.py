import time

import cv2
import datetime
import pandas as pd
df = pd.read_excel("C:/Users/Asus/Downloads/attendence2.xlsx")
#date=datetime.datetime.today().date()

date=input("Enter the date :")
df[date]='A'
# Save the updated DataFrame to the Excel file
df.to_excel("C:/Users/Asus/Downloads/attendence2.xlsx", index=False)
df