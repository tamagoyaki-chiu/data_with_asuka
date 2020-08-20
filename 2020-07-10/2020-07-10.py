import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 讀取圖片
'''
m1 = cv2.imread("1.jpg", 1) #後面的0-2就是黑到白 灰階
# m1 = cv2.cvtColor(m1, cv2.COLOR_BGR2HSV) #BGR轉HSV
m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
# m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY) #BGR轉灰階 
# m1 = cv2.cvtColor(m1, cv2.COLOR_GRAY2BGR) #GRAY轉BGR
cv2.imwrite("2.jpg", m2)
#畫質不影響的話就用png
cv2.imwrite("8.jpg", m2, [cv2.IMWRITE_JPEG_QUALITY, 100])

print(m1.shape[0])
print(m1.shape[1])
print(m1.shape)

print(m2.shape[0]) #高
print(m2.shape[1]) #寬
print(m2.shape)

cv2.imshow("Photo - 1", m1)
cv2.imshow("Photo - 1", m2)
cv2.waitKey(0)
cv2.destroyAllWindows()
write("4.jpg", m1, [cv2.IMWRITE_JPEG_QUALITY, 0])
cv2.imwrite("3.jpg", m1, [cv2.IMWRITE_JPEG_QUALITY, 50])
cv2.imwrite("5.jpg", m1, [cv2.IMWRITE_JPEG_QUALITY, 100]) 

cv2.imwrite("6.jpg", m2, [cv2.IMWRITE_JPEG_QUALITY, 0])
cv2.imwrite("7.jpg", m2, [cv2.IMWRITE_JPEG_QUALITY, 50])

'''

# 讀攝影機
'''
p1 = cv2.VideoCapture(0)
while p1.isOpened()==True:
    ret, m1=p1.read() #有沒有讀到圖片 有兩個變數 True/False
    cv2.imshow("Photo - 1", m1)
    if cv2.waitKey(33)!=-1: #每秒顯示幀數(FPS) eg. 每分鐘一千毫秒 除以30 約等於33.33 所以寫33
        break
cv2.destroyAllWindows() 
'''
# 讀影片
'''
p1 = cv2.VideoCapture("dog.mp4")
print("高:", p1.get(4))
print("寬:", p1.get(3))
print("總影格:", p1.get(7))
print("FPS:", p1.get(5))

p1.set(1,1234) #當前的影格

while p1.isOpened()==True:
    ret, m1=p1.read() #有沒有讀到圖片 有兩個變數 True/False
    if ret==True:
        print("當前影格:",p1.get(1))
        cv2.imshow("Photo - 1", m1)
        if cv2.waitKey(33)!=-1: #每秒顯示幀數(FPS) eg. 每分鐘一千毫秒 除以30 約等於33.33 所以寫33
            break  #從這格開始播放
        else:  #播了這格就關起來 沒有else這兩行就可以繼續播
            break  
cv2.destroyAllWindows()
'''
# 把攝影機畫面存成影片 或是把影片擷取特定的影格 擷取一小段
'''
p1 = cv2.VideoCapture("Asuka_magic.mp4")
print("高:", p1.get(4))
print("寬:", p1.get(3))
print("總影格:", p1.get(7))
print("FPS:", p1.get(5))
f = cv2.VideoWriter_fourcc(*'MP4V')
w = int(p1.get(3))  # 傳回來的長寬會是小數 所以要int成整數下面才能用
h = int(p1.get(4))
p2 = cv2.VideoWriter("part.mp4", f, 40, (w, h))
i = 0  # 設參數給後面只錄一小段用
while p1.isOpened() == True:
    ret, m1 = p1.read()  # 有沒有讀到圖片 有兩個變數 True/False
    if ret == True:
        i += 1
        if i > 2000 and i <= 2400:
            p2.write(m1)
            # 第三秒錄到第十秒 (30fps*3(第三秒) 所以是90) 
        cv2.imshow("Image 1", m1)
        if cv2.waitKey(33) != -1:  # 每秒顯示幀數(FPS) eg. 每分鐘一千毫秒 除以30 約等於33.33 所以寫33
            break  # 從這格開始播放
        # else:  #播了這格就關起來 沒有else這兩行就可以繼續播
        #     break
p2.release()
cv2.destroyAllWindows()
'''
# 畫畫

m1 = np.full(
    (150, 300, 3),
    (150, 250, 180),
    np.uint8
)
cv2.line(m1, (30, 40), (50, 40), (0, 170, 0), 5)
cv2.line(m1, (30, 20), (30, 40), (0, 170, 0), 5)
cv2.line(m1, (50, 20), (50, 40), (0, 170, 0), 5)
cv2.line(m1, (70, 40), (90, 40), (0, 170, 0), 5)
cv2.line(m1, (70, 30), (90, 30), (0, 170, 0), 5)
cv2.line(m1, (70, 22), (70, 30), (0, 170, 0), 5)
cv2.line(m1, (90, 22), (90, 30), (0, 170, 0), 5)
cv2.line(m1, (80, 20), (80, 40), (0, 170, 0), 5)

cv2.circle(m1, (125, 30), 20, (0, 170, 0), 2)  # 畫圓形

m1 = Image.fromarray(m1)

f = ImageFont.truetype("msgothic.ttc", 50)
ImageDraw.Draw(m1).text((50, 70), "齋藤飛鳥", (0, 87, 87), f)
m1 = np.array(m1)

cv2.imshow("Image 1", m1)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
m1 = cv2.imread("1.jpg", 1)
# m2=np.full(m1.shape,100,np.uint8)

# m3=cv2.add(m1,m2) #加法最高是加到白色
# m3=cv2.subtract(m1,m2)
# m3=cv2.absdiff(m1,m2)
# m3=cv2.divide(m1,m2)
# m3=cv2.multiply(m3,m2)
# m3=cv2.bitwise_not(m3,m2) #not 指令 色相相反
# m3=m1+255
# w=300
# h=int((w/m1.shape[1])*m1.shape[0])
# h=300
# w=int((h/m1.shape[0])*m1.shape[1])

#m2=cv2.flip(m1,-1)
# d=cv2.getRotationMatrix2D((300,300)), 45, 1)
# m2=cv2.warpAffine(m1, d, (500,500))

m1 = cv2.imread("image/1.jpg", 1)
m2 = np.full(m1.shape,255,np.uint8)
# m2[100:250,100:250]=m1[50:200,100:250]
# m2[:,100:250]=m1[:,100:250]  #高度都留著 切寬度而已
m1[50:200,100:250]=255

cv2.imshow("Image 1", m1[:,:,2])
cv2.imshow("Image 2", m2)
# cv2.imshow("Image 3",m3)
cv2.imshow("Image 2", m1[50:200,100:250]) #裁切
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
