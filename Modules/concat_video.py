import cv2
import numpy as np
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
cap = cv2.VideoCapture('SSD_module_wander_low_th_0_max5_5fps_.avi',0)
cap1 = cv2.VideoCapture('SSD_module_wander_low_th_3_max1_5fps_.avi',0)
out = cv2.VideoWriter('concat1.avi', fourcc, 6.0, (int(1280), int(360)))
count=0
while(cap.isOpened()):
    
    
    ret, frame = cap.read()
    ret1, frame1 = cap1.read()
    if ret == True and ret1 == True: # you *have* to check *both* captures ! 
        h,w,c = frame.shape;
        h1,w1,c1 = frame1.shape;

        if h != h1 or w != w1: # resize right img to left size
            frame1 = cv2.resize(frame1,(w,h))
        count+=1
        print(count)
        both = np.concatenate((frame, frame1), axis=1)
        # out1 = cv2.VideoWriter('concat2.avi', cv2.VideoWriter_fourcc(*'XVID'), cap.get(cv2.CAP_PROP_FPS), (2 * w,h))
        # out1.write(both)
        out.write(both)
    else: 
        break

cap.release()
out.release()
out1.release()


