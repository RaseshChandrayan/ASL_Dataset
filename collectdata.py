import cv2
import os
import cvzone.HandTrackingModule 


directory= 'SignImage200x200/'
print(os.getcwd())

if not os.path.exists(directory):
    os.mkdir(directory)
if not os.path.exists(f'{directory}/blank'):
    os.mkdir(f'{directory}/blank')
    

#for i in range(65,91):
 #   letter  = chr(i)
  #  if not os.path.exists(f'{directory}/{letter}'):
   #     os.mkdir(f'{directory}/{letter}')


import os
import cv2
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/A")),
             'b': len(os.listdir(directory+"/B")),
             'c': len(os.listdir(directory+"/C")),
             'e': len(os.listdir(directory+"/E")),
             'i': len(os.listdir(directory+"/I")),
             'v': len(os.listdir(directory+"/V")),
             'w': len(os.listdir(directory+"/W")),
             'y': len(os.listdir(directory+"/Y")),
             }

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,300),(255,255,255),2)
    cv2.imshow("data",frame)
    frame=frame[40:300,0:300]
    cv2.imshow("ROI",frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(200,200))
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(directory+'A/'+str(count['a']))+'.jpg',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(os.path.join(directory+'B/'+str(count['b']))+'.jpg',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(os.path.join(directory+'C/'+str(count['c']))+'.jpg',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(os.path.join(directory+'E/'+str(count['e']))+'.jpg',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(os.path.join(directory+'I/'+str(count['i']))+'.jpg',frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(os.path.join(directory+'V/'+str(count['v']))+'.jpg',frame)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(os.path.join(directory+'W/'+str(count['w']))+'.jpg',frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(os.path.join(directory+'Y/'+str(count['y']))+'.jpg',frame)
    