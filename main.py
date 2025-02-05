import cv2
#
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
if cap.isOpened()==False:
    print("ERROR!IN OPENING THE CAMERA")
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        print("ERROR!!!")
        break
    GRAY=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(GRAY,minNeighbors=6,minSize=(30,30),scaleFactor=1.1)
    startpoint=(30,30)
    height=40
    width=80
    endpoint=(30+width,30+height)
    cv2.rectangle(frame,startpoint,endpoint,thickness=5,color="blue")
    cv2.imshow("face detection!!,press 'q' to quit",frame)
    if cv2.waitKey(1) and 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    