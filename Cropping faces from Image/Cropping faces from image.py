import cv2                           #importing cv library
import numpy as np                   #importing numpy library as np                      

path = input('Enter the path for image')  #get the input for image path
img = cv2.imread(path)
  
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h),      #Drawing rectangles around the detected faces
                  (0, 0, 255), 2)
      
    faces = img[y:y + h, x:x + w]
    cv2.imshow('faces',faces)      #Showing the detected faces in a cropped manner
   
  
cv2_imshow('Original Image', img)   #Showing the original Image
cv2.waitKey()
cv2.destroyAllWindows()
