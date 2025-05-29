import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector


cap=cv2.VideoCapture(0)
detector=HandDetector(staticMode=False,maxHands=2,modelComplexity=1,detectionCon=0.5,minTrackCon=0.5)

while True:
   success, img=cap.read()
   if not success:
      break 
   hands, img=detector.findHands(img,flipType=True)
 
   if hands:
      for hand in hands:
         handType=hand["type"]
         fingers=detector.fingersUp(hand)
         fc=fingers.count(1)
         bbox=hand["bbox"]
         x,y=bbox[0],bbox[1]
         text=f'{handType} Hand'
         ctext=f'fingers up:{fc}'
         cv2.putText(img,text,(x,y-65),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
         cv2.putText(img,ctext,(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
   cv2.imshow("img",img)
   if cv2.waitKey(1) & 0xFF == ord("q"):
      break
      
cap.release()
cv2.destroyAllWindows()

