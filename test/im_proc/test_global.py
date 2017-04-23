import sys
sys.path[0] = sys.path[0].replace('/test/im_proc','')

import imageproc.image_processing as IMPROC

for i in sys.argv[1:] :
    exec(i)

#script de test
image1 = "2.jpg"
image2 = "3.jpg"

print()
print('######################')
IMPROC.init_imageproc()
IMPROC.distance_crossed(image1,image2)
print('######################')
print()
