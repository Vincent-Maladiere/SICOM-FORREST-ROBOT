import math
import cv2
import numpy as np

def find_2_opposite_points(mask):

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

	return [x1, y1, x2, y2]


def a4_diago(image, threshold_hl, threshold_hh,threshold_sl,threshold_vl):

	i = cv2.imread(image,1)
	hsv = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)
	low_green = np.array([threshold_hl,threshold_sl,threshold_vl])
	high_green= np.array([threshold_hh,255,255])
	mask = cv2.inRange(hsv, low_green, high_green)

	X = find_2_opposite_points(mask)
	x1 = X[0]
	x2 = X[2]
	y1 = X[1]
	y2 = X[3]

	d = math.sqrt((x1-x2)**2+(y1-y2)**2)

	cv2.imshow('mask',mask)
	
	#the two found vertexes in black :
	i[x1,y1,0]=0
    	i[x1,y1,1]=0
	i[x1,y1,2]=0
	i[x2,y2,0]=0
	i[x2,y2,1]=0
	i[x2,y2,2]=0

	cv2.imshow('image_vertexes',i)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return d


def position(image, threshold_hl, threshold_hh, threshold_sl, threshold_vl):

	i = cv2.imread(image,1)
	hsv = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)
	low_green = np.array([threshold_hl,threshold_sl,threshold_vl])
	high_green= np.array([threshold_hh,255,255])
	mask = cv2.inRange(hsv, low_green, high_green)

	cv2.imshow('mask',mask)

	X = find_2_opposite_points(mask)
	x1 = X[0]
	x2 = X[2]
	y1 = X[1]
	y2 = X[3]

	#the middle point of the figure :
	x3 = (x1+x2)/2
	y3 = (y1+y2)/2

	#in black :
	i[x3,y3,0]=0
    	i[x3,y3,1]=0
	i[x3,y3,2]=0

	cv2.imshow('image_middle_point',i)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return [x3,y3]

def distance_crossed(image1, image2,threshold_hl_green, threshold_hh_green, threshold_hl_red, threshold_hh_red, threshold_sl, threshold_vl):

	#scale, cartesian distance <=> real distance
	a4rd = 36.3 #cm
	a4cd = a4_diago(image1, threshold_hl_green, threshold_hh_green, threshold_sl, threshold_vl)

	[x1, y1] = position(image1, threshold_hl_red, threshold_hh_red, threshold_sl, threshold_vl)
	[x2, y2] = position(image2, threshold_hl_red, threshold_hh_red, threshold_sl, threshold_vl)
	
	cd = math.sqrt((x1-x2)**2+(y1-y2)**2)   #castesian distance
	rd = cd * a4rd/a4cd			#real distance in cm

	return rd
