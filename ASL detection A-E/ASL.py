import cvzone
import cv2
from cvzone.ClassificationModule import Classifier

cap=cv2.VideoCapture(0)
path=".\ASL detection A-E"
cla=Classifier(f'{path}\keras_model.h5',f'{path}\labels.txt')

while True:
    success, img=cap.read()
    if not success:
        break
    img=cv2.flip(img,1)
    prediction=cla.getPrediction(img)
    print(prediction)
    cv2.imshow("ASL detection",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break

cap.release()
cv2.destroyAllWindows()



