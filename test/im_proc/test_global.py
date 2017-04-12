import sys
sys.path[0] = sys.path[0].replace('/test/im_proc','')

import parameters as PA
import imageproc.image_processing as IMPROC

#script
image1 = "2.jpg"
image2 = "3.jpg"

IMPROC.init_imageproc(PA.MODE)
IMPROC.distance_crossed(image1,image2,PA.MODE)
