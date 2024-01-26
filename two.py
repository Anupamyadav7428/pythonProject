import cv2 
import os
from PIL import Image
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "C:/Users/Asus/image detect"

def getImagesWithId(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []

    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow('training', faceNp)
        cv2.waitKey(100)

    return np.array(IDs), faces

Ids, faces = getImagesWithId(path)

# Check if there are faces for training
if len(Ids) == 0 or len(faces) == 0:
    print("No faces found for training.")
else:
    recognizer.train(faces, np.array(Ids))
    recognizer.save("C:/Users/Asus/training.yml")

cv2.destroyAllWindows()
