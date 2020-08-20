import cv2
import numpy as np
import pytesseract as pt
from pyzbar import pyzbar

# m1 = cv2.imread("7.jpg", 1)

# ret = pt.image_to_string(m1, "1231", "eng")
# print(ret)

# cv2.imshow("Image 1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# m1 = cv2.imread("5.jpg", 1)
# m2 = cv2.inRange(m1, (240,240,240),(255, 255, 255))
# m2 = cv2.erode(m2, np.ones((2,15)))
# a, b=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# for i in range(1, len(a)):
#     x, y, w, h = cv2.boundingRect(a[i])
#     m3=cv2.inRange(m1[y:y+h,x:x+w],(32,69,220),(72,109,255))
#     m3=cv2.dilate(m3, np.ones((5,12)))  #白色放大
#     c, d=cv2.findContours(m3,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#     if len(c)==4:  #有東西 就取長度 數量 =4(因為塗上有4個橘色字) 總共有4個輪廓
#         m4=m1[y:y+h,x:x+w]
#         h=50
#         w=int((h/m4.shape[0])*m4.shape[1])
#         m4=cv2.resize(m4, (w,h))

#         m5=np.full((m4.shape[0]+100,m4.shape[1]+100,3),255,np.uint8)
#         m5[50:m4.shape[0]+50,50:m4.shape[1]+50]=m4

#         ret = pt.image_to_string(m1, "eng", "")
#         print(ret)
#         cv2.imwrite("./"+str(i)+".jpg",m5)
#         cv2.imshow("Image 4"+str(i), m5)

# m1=cv2.imread("image/9.png",1)

# ret=pyzbar.decode(m1)
# for d in ret:
#     print("條碼類型:",d.type)
#     print("條碼內容:",d.data.decode("utf8").encode("sjis").decode("urf8"))
#     x,y,w,h=d.rect
#     cv2.rectangle(m1,(x,y),(x+w,y+h), (0,0,255),2)
#     print("=======================================")

# p1 = cv2.VideoCapture(0)
# while p1.isOpened()==True:
#     ret2, m1=p1.read() #有沒有讀到圖片 有兩個變數 True/False
#     if ret2==True:

#         ret=pyzbar.decode(m1)
#         for d in ret:
#             print("條碼類型:",d.type)
#             try:
#                 print("條碼內容:",d.data.decode("utf8").encode("sjis").decode("urf8"))
#             except:
#                 print("條碼內容:",d.data.decode("utf8"))
#             x,y,w,h=d.rect
#             cv2.rectangle(m1,(x,y),(x+w,y+h), (0,0,255),2)
#             print("=======================================")
#         cv2.imshow("Image 1", m1)
#         if cv2.waitKey(33)!=-1: #每秒顯示幀數(FPS) eg. 每分鐘一千毫秒 除以30 約等於33.33 所以寫33
#             break
# cv2.destroyAllWindows() 

#人臉辨識

p1 = cv2.imread("9.png", 1)

control=cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
while p1.isOpened()==True:
    ret2, m1=p1.read() #有沒有讀到圖片 有兩個變數 True/False
    if ret2==True:
        returnA=control.detectMultiScale(
            m1,
            minNeighbors=1,
            minSize=(3,3)
        )
        for x,y,width,height in returnA:
            cv2.rectangle(m1, (x,y), (x+width,y+height), (0,0,255),2)

        cv2.imshow("Image 1", m1)
        if cv2.waitKey(33)!=-1: #每秒顯示幀數(FPS) eg. 每分鐘一千毫秒 除以30 約等於33.33 所以寫33
            break
    else:
        break
cv2.destroyAllWindows() 

