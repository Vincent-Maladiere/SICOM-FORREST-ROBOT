import sys
sys.path[0] = sys.path[0].replace('/test/im_proc','')

import parameters as PA
import imageproc.image_processing as IMPROC

for i in sys.argv[1:] :
    exec(i)

#script de test
print()
print('######################')
IMPROC.init_imageproc(IMPROC.DISPLAY)
print('######################')
print()
