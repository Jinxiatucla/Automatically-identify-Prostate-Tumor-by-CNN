import cv2
import numpy as np
from collections import Counter

def prune_image(mask,image):
 '''
 input: image ans corresponding masks
 output: images pruned according to masks
 '''
 a = cv2.imread(mask, 0)
 b = np.asarray(a)
 img = cv2.imread(image, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
 min_r = 128
 max_r = 127
 min_c = 128
 max_c = 127

 for i in range(0, 255):
    for j in range(0, 255):
         if b[i,j] >  40:
             print('true')
             if i < min_r:
                 min_r = i
             elif i > max_r:
                 max_r = i
             if j < min_c:
                 min_c = j
             elif j > max_c:
                 max_c = j


 pruned_img = img[min_r:max_r,min_c:max_c, :]
 return pruned_img

#prune 61 image inside folder
for i in range(62):
 mask = '../unaugmented_DATA/mask_prediction/mask/mask_0.png'.replace('0',str(i))
 img = '../unaugmented_DATA/mask_prediction/image/image_0.png'.replace('0',str(i))
 a = prune_image(mask,img)
 b = cv2.resize(a, (227, 227),interpolation = cv2.INTER_AREA)
 cv2.imwrite(''+ str(i) +'.png', b)




