import cv2
import numpy as np
from tkinter import *

#pysimplegui installed


def nothing(x):
    pass


cv2.namedWindow('marking')
cv2.resizeWindow("marking", 500, 400)

cv2.createTrackbar('H Lower','marking',0,179,nothing)
cv2.createTrackbar('H Higher','marking',179,179,nothing)
cv2.createTrackbar('S Lower','marking',0,255,nothing)
cv2.createTrackbar('S Higher','marking',255,255,nothing)
cv2.createTrackbar('V Lower','marking',0,255,nothing)
cv2.createTrackbar('V Higher','marking',255,255,nothing)
print('SAVE HSV RANGE -> a')



while True:
  img=cv2.imread("lego-rotXX-8a.jpg")
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



  hL = cv2.getTrackbarPos('H Lower','marking')
  hH = cv2.getTrackbarPos('H Higher','marking')
  sL = cv2.getTrackbarPos('S Lower','marking')
  sH = cv2.getTrackbarPos('S Higher','marking')
  vL = cv2.getTrackbarPos('V Lower','marking')
  vH = cv2.getTrackbarPos('V Higher','marking')

  LowerRegion = np.array([hL,sL,vL],np.uint8)
  upperRegion = np.array([hH,sH,vH],np.uint8)

  Object = cv2.inRange(hsv,LowerRegion,upperRegion)

  kernal = np.ones((1,1),"uint8")

  detected = cv2.morphologyEx(Object,cv2.MORPH_OPEN,kernal)
  detected = cv2.dilate(detected,kernal,iterations=1)

  res1=cv2.bitwise_and(img, img, mask = detected)
  res1=cv2.resize(res1, (900, 600))
  cv2.imshow("Masking",res1)


  if cv2.waitKey(33) == ord('a'):
        print("Guardar")

        hL = cv2.getTrackbarPos('H Lower', 'marking')
        hH = cv2.getTrackbarPos('H Higher', 'marking')
        sL = cv2.getTrackbarPos('S Lower', 'marking')
        sH = cv2.getTrackbarPos('S Higher', 'marking')
        vL = cv2.getTrackbarPos('V Lower', 'marking')
        vH = cv2.getTrackbarPos('V Higher', 'marking')


        stringhL= str(hL)
        stringsL= str(sL)
        stringvL= str(vL)
        stringhH= str(hH)
        stringsH = str(sH)
        stringsvH = str(vH)


        LowerRegion = np.array([hL, sL, vL], np.uint8)
        upperRegion = np.array([hH, sH, vH], np.uint8)

        Object = cv2.inRange(hsv, LowerRegion, upperRegion)

        kernal = np.ones((1, 1), "uint8")

        detected = cv2.morphologyEx(Object, cv2.MORPH_OPEN, kernal)
        detected = cv2.dilate(detected, kernal, iterations=1)

        res1 = cv2.bitwise_and(img, img, mask=detected)
        res1 = cv2.resize(res1, (900, 600))
        cv2.imshow("Masking", res1)

        str1 = str(LowerRegion) + "  \n", str(upperRegion) + " \n"

        nomeFile= input("Inserir cor! \n")
        print(nomeFile)
        f=open(nomeFile,"w")

        str2=str("Samuel")

        f.writelines(stringhL)
        f.writelines('\n')
        f.writelines(stringsL)
        f.writelines('\n')
        f.writelines(stringvL)
        f.writelines('\n')
        f.writelines(stringhH)
        f.writelines('\n')
        f.writelines(stringsH)
        f.writelines('\n')
        f.writelines(stringsvH)

        f.close()

        #f = open("yellowMask.txt", "w")
        #f.writelines(str1)
        #f.close()

  if cv2.waitKey(10) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break


