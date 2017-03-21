import math
import cv2
import numpy as np

#mode 0 with picture display
#mode 1 without picture display


def find_2_opposite_points(mask):	#find to two opposite points on a mask, one on the left at the top, the other on the right at the bottom

     [X,Y]=mask.shape
     x1 = 0
     y1 = 0
     while mask[x1,y1]==0:
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



def a4_diago(image, threshold_hl, threshold_hh,threshold_sl,threshold_vl, mode):#return castesian length of the diagonal of the sheet paper

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

     if(mode == 0):
          
          #the two found vertexes in black :
          i[x1,y1,0]=0
          i[x1,y1,1]=0
          i[x1,y1,2]=0
          i[x2,y2,0]=0
          i[x2,y2,1]=0
          i[x2,y2,2]=0
          
          cv2.imshow('mask',mask)
          cv2.imshow('image_vertexes',i)

          cv2.waitKey(0)
          cv2.destroyAllWindows()

     return d



def find_position(image, threshold_green_hl, threshold_green_hh,threshold_green_sl, threshold_red_hl, threshold_red_hh,threshold_red_sl, threshold_vl, mode):
     
     i = cv2.imread(image,1)
     hsv = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)

     low_green = np.array([threshold_green_hl,threshold_green_sl,threshold_vl])
     high_green= np.array([threshold_green_hh,255,255])
     maskg = cv2.inRange(hsv, low_green, high_green)

     low_red = np.array([threshold_red_hl,threshold_red_sl,threshold_vl])
     high_red= np.array([threshold_red_hh,255,255])
     maskr = cv2.inRange(hsv, low_red, high_red)

     if(mode == 0):
          cv2.imshow('image_with_detected_dots',i)
          cv2.imshow('maskg',maskg)
          cv2.imshow('maskr',maskr)
          cv2.waitKey(0)
          cv2.destroyAllWindows()

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



def main(image1, image2, image3, threshold_green_hl, threshold_green_hh,threshold_green_sl, threshold_red_hl, threshold_red_hh,threshold_red_sl, threshold_vl, mode):
     
     #scale, cartesian distance <=> real distance      (has to run one time only at the beginning of the test series)
     a4rd = 36.3 #cm
     a4cd = a4_diago(image1, threshold_green_hl, threshold_green_hh, threshold_green_sl, threshold_vl, mode)

     #initial position
     [(xg,yg),(xr,yr)] = find_position(image2, threshold_green_hl, threshold_green_hh,threshold_green_sl, threshold_red_hl, threshold_red_hh,threshold_red_sl, threshold_vl, mode)
     [xo,yo] = [(xg+xr)/2,(yg+yr)/2]

     #final position
     [(xgq,ygq),(xrq,yrq)] = find_position(image3, threshold_green_hl, threshold_green_hh,threshold_green_sl, threshold_red_hl, threshold_red_hh,threshold_red_sl, threshold_vl, mode)
     (xq,yq) = ((xgq+xrq)/2,(ygq+yrq)/2)

     i = cv2.imread(image3,1)
     hsv = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)

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

     #projection (orthogonality and cartesian equation verification)
     xp = (xq*(xr-xg)*(xr-xg)+xg*(yr-yg)*(yr-yg)+(yq-yg)*(yr-yg)*(xr-xg))/((xr-xg)*(xr-xg)+(yr-yg)*(yr-yg))
     yp = yg+(xp-xg)*(yr-yg)/(xr-xg)

     if(mode == 0):
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

          i[xo,yo,0]=0
          i[xo,yo,1]=0
          i[xo,yo,2]=255

          i[xo+1,yo,0]=0
          i[xo+1,yo,1]=0
          i[xo+1,yo,2]=255

          i[xo-1,yo,0]=0
          i[xo-1,yo,1]=0
          i[xo-1,yo,2]=255

          i[xo,yo+1,0]=0
          i[xo,yo+1,1]=0
          i[xo,yo+1,2]=255

          i[xo,yo-1,0]=0
          i[xo,yo-1,1]=0
          i[xo,yo-1,2]=255

          i[xq,yq,0]=0
          i[xq,yq,1]=0
          i[xq,yq,2]=0
     
          cv2.imshow('Initial and projected final position in red',i)
          cv2.waitKey(0)
          cv2.destroyAllWindows()

     d = math.sqrt((xq-xo)*(xq-xo)+(yq-yo)*(yq-yo))*a4rd/a4cd
     dp = math.sqrt((xp-xo)*(xp-xo)+(yp-yo)*(yp-yo))*a4rd/a4cd

     print("Forrest has travelled a distance of ",d," cm.")

     if((xr >= xo and xp >= xo and yr >= yo and yp >= yo) or (xr <= xo and xp <= xo and yr >= yo and yp >= yo) or (xr <= xo and xp <= xo and yr <= yo and yp <= yo) or (xr >= xo and xp >= xo and yr <= yo and yp <= yo)):
          print("He has travelled a distance of ",dp," cm in the right direction.")
          return [d,dp,1]
     else:
          print("He has travelled a distance of ",dp," cm in the wrong direction.")
          return [d,dp,0]
