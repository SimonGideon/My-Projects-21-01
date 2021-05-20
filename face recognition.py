import cv
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_dafault.xml')
cap = cv.Videocapture(0)
while True:
    _, img = cap.read()
    gray = cv.cvtcolor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv.imshow('img', img)
    k = cv.waitkey(30) & 0xff
    if k==27:
        break
cap.release()
