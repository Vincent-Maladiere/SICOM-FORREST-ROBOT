import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import parameters as PA

THRES_G_HUE_LOWER = 40      #green
THRES_G_HUE_UPPER = 60
THRES_G_SAT_LOWER = 20

THRES_R_HUE_LOWER = 0       #red
THRES_R_HUE_UPPER = 15
THRES_R_SAT_LOWER = 100

THRES_VALUE_LOWER = 200

DISPLAY = 0              #mode 0 with picture display
NO_DISPLAY = 1           #mode 1 without picture display
A4_CART_DIAGO = 0        #cartesian length of the diagonal of the sheet paper
A4_REAL_DIAGO = 36.3     #cm

def find_2_opposite_points(mask):	#find to two opposite points on a mask, one on the left at the top, the other on the right at the bottom

     [X,Y]=mask.shape
     x1 = 0
     y1 = 0
     cornerMask = cv2.cornerHarris(mask,2,7,0.04)
     cornerMask = cornerMask>0.01*cornerMask.max()
     i = 0
     e = [k for k,x in enumerate(cornerMask[i]) if x== True]
     while e == []:
          i = i+1
          e = [k for k,x in enumerate(cornerMask[i]) if x== True]

     p1 = [i, e[0]]

     i = X-1
     e = [k for k,x in enumerate(cornerMask[i]) if x== True]
     while e == []:
          i = i-1
          e = [k for k,x in enumerate(cornerMask[i]) if x== True]

     p2 = [i, e[0]]

     return [p1[0], p1[1], p2[0], p2[1]]



def a4_diago(image, mode):     #return cartesian length of the diagonal of the sheet paper

     i = cv2.imread(image,1)
     hsv = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)
     low_green = np.array([THRES_G_HUE_LOWER,THRES_G_SAT_LOWER,THRES_VALUE_LOWER])
     high_green= np.array([THRES_G_HUE_UPPER,255,255])
     mask = cv2.inRange(hsv, low_green, high_green)

     X = find_2_opposite_points(mask)
     x1 = X[0]
     x2 = X[2]
     y1 = X[1]
     y2 = X[3]

     d = math.sqrt((x1-x2)**2+(y1-y2)**2)

     if(mode == DISPLAY):
          
          #the two found vertexes in black :
          i[x1,y1,0]=0
          i[x1,y1,1]=0
          i[x1,y1,2]=0
          i[x2,y2,0]=0
          i[x2,y2,1]=0
          i[x2,y2,2]=0
          
          plt.imshow(mask)
          plt.show()
          plt.imshow(i)
          plt.show()

     return d



def find_position(image, mode):
     
     i = cv2.imread(image,1)
     hsv = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)

     low_green = np.array([THRES_G_HUE_LOWER,THRES_G_SAT_LOWER,THRES_VALUE_LOWER])
     high_green= np.array([THRES_G_HUE_UPPER,255,255])
     maskg = cv2.inRange(hsv, low_green, high_green)

     low_red = np.array([THRES_R_HUE_LOWER,THRES_R_SAT_LOWER,THRES_VALUE_LOWER])
     high_red= np.array([THRES_R_HUE_UPPER,255,255])
     maskr = cv2.inRange(hsv, low_red, high_red)

     if(mode == DISPLAY):
          plt.imshow(i)
          plt.show()
     
     #green dot :
     Xg = find_2_opposite_points(maskg)
     x1g = Xg[0]
     x2g = Xg[2]
     y1g = Xg[1]
     y2g = Xg[3]

     #the middle point of the green dot :
     x3g = (x1g+x2g)/2
     y3g = (y1g+y2g)/2

     #red dot :
     Xr = find_2_opposite_points(maskr)
     x1r = Xr[0]
     x2r = Xr[2]
     y1r = Xr[1]
     y2r = Xr[3]

     #the middle point of the red dot :
     x3r = (x1r+x2r)/2
     y3r = (y1r+y2r)/2

     return [(x3g,y3g),(x3r,y3r)]


def init_imageproc(image1, mode):

     global A4_CART_DIAGO
     A4_CART_DIAGO = a4_diago(image1, mode)
     

def distance_crossed(image2, image3, mode):
     
     #initial position
     [(xg,yg),(xr,yr)] = find_position(image2, mode)
     [xo,yo] = [(xg+xr)/2,(yg+yr)/2]

     #final position
     [(xgq,ygq),(xrq,yrq)] = find_position(image3, mode)
     (xq,yq) = ((xgq+xrq)/2,(ygq+yrq)/2)

     i = cv2.imread(image3,1)
     hsv = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)

     #projection (orthogonality and cartesian equation verification)
     xp = (xq*(xr-xg)*(xr-xg)+xg*(yr-yg)*(yr-yg)+(yq-yg)*(yr-yg)*(xr-xg))/((xr-xg)*(xr-xg)+(yr-yg)*(yr-yg))
     yp = yg+(xp-xg)*(yr-yg)/(xr-xg)

     if(mode == DISPLAY):
          #axe drawing
          [L,H,D]=i.shape
          k=0
          while(k < L):
               l=0
               while(l < H):
                    if(((l-yg)+(xg-k)*(yr-yg)/(xr-xg)) == 0):
                         i[k,l,0]=0
                         i[k,l,1]=0
                         i[k,l,2]=0
                    l = l+1
               k=k+1

          i[int(round(xp)),int(round(yp)),0]=0
          i[int(round(xp)),int(round(yp)),1]=0
          i[int(round(xp)),int(round(yp)),2]=255

          i[int(round(xp))+1,int(round(yp)),0]=0
          i[int(round(xp))+1,int(round(yp)),1]=0
          i[int(round(xp))+1,int(round(yp)),2]=255

          i[int(round(xp))-1,int(round(yp)),0]=0
          i[int(round(xp))-1,int(round(yp)),1]=0
          i[int(round(xp))-1,int(round(yp)),2]=255

          i[int(round(xp)),int(round(yp))+1,0]=0
          i[int(round(xp)),int(round(yp))+1,1]=0
          i[int(round(xp)),int(round(yp))+1,2]=255

          i[int(round(xp)),int(round(yp))-1,0]=0
          i[int(round(xp)),int(round(yp))-1,1]=0
          i[int(round(xp)),int(round(yp))-1,2]=255

          xoe = int(round(xo))
          yoe = int(round(yo))
          xqe = int(round(xq))
          yqe = int(round(yq))

          i[xoe,yoe,0]=0
          i[xoe,yoe,1]=0
          i[xoe,yoe,2]=255

          i[xoe+1,yoe,0]=0
          i[xoe+1,yoe,1]=0
          i[xoe+1,yoe,2]=255

          i[xoe-1,yoe,0]=0
          i[xoe-1,yoe,1]=0
          i[xoe-1,yoe,2]=255

          i[xoe,yoe+1,0]=0
          i[xoe,yoe+1,1]=0
          i[xoe,yoe+1,2]=255

          i[xoe,yoe-1,0]=0
          i[xoe,yoe-1,1]=0
          i[xoe,yoe-1,2]=255

          i[xqe,yqe,0]=0
          i[xqe,yqe,1]=0
          i[xqe,yqe,2]=0
     
          plt.imshow(i)
          plt.show()
          
     d = math.sqrt((xq-xo)*(xq-xo)+(yq-yo)*(yq-yo))*A4_REAL_DIAGO/A4_CART_DIAGO
     dp = math.sqrt((xp-xo)*(xp-xo)+(yp-yo)*(yp-yo))*A4_REAL_DIAGO/A4_CART_DIAGO

     print("Forrest has travelled a distance of ",d," cm.")

     if((xr >= xo and xp >= xo and yr >= yo and yp >= yo) or (xr <= xo and xp <= xo and yr >= yo and yp >= yo) or (xr <= xo and xp <= xo and yr <= yo and yp <= yo) or (xr >= xo and xp >= xo and yr <= yo and yp <= yo)):
          print("He has travelled a distance of ",dp," cm in the right direction.")
          return dp
     else:
          print("He has travelled a distance of ",dp," cm in the wrong direction.")
          dp = -1*dp
          return dp

