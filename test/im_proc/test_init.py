import sys
sys.path[0] = sys.path[0].replace('/test/im_proc','')

import parameters as PA
import imageproc.image_processing as IMPROC

#script
IMPROC.init_imageproc("DISPLAY")

