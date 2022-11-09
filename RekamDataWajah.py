import cv2
wajahDir = 'datawajah'
cam = cv2.VideoCapture(0)
cam.set(3,640) #lebar
cam.set(4,480) #tinggi2
facedetetor = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeDetetor  = cv2.CascadeClassifier('haarcascade_eye.xml')
faceID = input("Masukan Face ID yang akan direkam datanya [kemudian tekan ENTER] :  ")
print("Tatap Wajah ke depan webcame. Tunggu proses pengambilan data wajah selesai...")
ambilData = 1

while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = facedetetor.detectMultiScale(abuAbu,1.3,5)
    for(x,y,w,h) in face:
        frame =cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        namaFile = 'wajah.'+str(faceID)+'.'+str(ambilData)+'.jpg'
        cv2.imwrite(wajahDir +'/'+namaFile,frame)
        ambilData += 1
        roiAbuAbu = abuAbu[y:y+h,x:x+w]
        roiWarna  = frame[y:y+h,x:x+w]
        eyes = eyeDetetor.detectMultiScale(roiAbuAbu)
        for (xe,ye,we,he) in eyes:
            cv2.rectangle(roiWarna,(xe,ye),(xe+we,ye+he),(0,0,255),2)
                       
    cv2.imshow('webcamku',frame)
    #cv2.imshow('webcamku-gray',abuAbu)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
    elif ambilData>30:
        break
print("Pengambilan Data Selesai")
cam.release()
cv2.destroyAllWindows()