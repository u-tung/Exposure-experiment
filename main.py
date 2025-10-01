import numpy as np
import cv2
import random
import glob

img = cv2.imread(glob.glob('*.jpg')[0])

print(img.shape[:-1])
#cv2.imshow('My Image', img)

whi = []

for cI in range(len(img)):

    for cII in range(len(img[cI])):

        if (img[cI, cII] != np.array([0, 0, 0])).all():

            whi += [ [cI, cII, img[cI, cII]] ]




random.shuffle(whi)
tI_img = img*0

all_fps = 60
showNum = len(whi)//all_fps
cI = 0
for cII in range(all_fps):

    for cIII in range(showNum):

        try:

            tI_img[whi[cI][0], whi[cI][1]] = whi[cI][2]
            cI += 1

        except IndexError:
            pass

    cv2.imwrite(f'img/{cII}.jpg', tI_img)
    tI_img = img*0

    
print(all_fps/3)
out = cv2.VideoWriter('t.mp4',cv2.VideoWriter_fourcc(*'mp4v'), all_fps//3, img.shape[1::-1])

for i in range(60):
    
    img = cv2.imread(f'img/{i}.jpg')
    
    out.write(img)
    
out.release()












