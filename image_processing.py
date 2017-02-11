import math
import cv2
import numpy as np

def a4_diago(image, threshold_hl, threshold_hh,threshold_sl,threshold_vl):

	i = cv2.imread(image,1)
	hsv = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)
	low_green = np.array([threshold_hl,threshold_sl,threshold_vl])
	high_green= np.array([threshold_hh,255,255])
	mask = cv2.inRange(hsv, low_green, high_green)

	[X,Y]=mask.shape


	x1 = 0
	y1 = 0
	while (mask[x1,y1]==0):
        	if y1 == Y-1:
            		x1 += 1
            		y1 = 1
        	else:
           		y1 += 1

	x2 = X-1
        y2 = Y-1
        while mask[x2,y2]==0:
        	if y2 == 1:
                	x2 -= 1
                	y2 = Y-1
        	else:
        	        y2 -= 1

	d=math.sqrt((x1-x2)**2+(y1-y2)**2)
	r = [x1,y1,x2,y2,d]

	cv2.imshow('image',i)
	cv2.imshow('mask',mask)
	
	#the two found vertexes in black

	i[x1,y1,0]=0
    	i[x1,y1,1]=0
	i[x1,y1,2]=0
	i[x2,y2,0]=0
	i[x2,y2,1]=0
	i[x2,y2,2]=0

	cv2.imshow('image_vertexes',i)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


	return r
