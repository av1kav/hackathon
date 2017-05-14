import os
import cv2

files = os.listdir()
for i in range(len(files)):
	if files[i].endswith('jpg'):
		image = cv2.imread(files[i],1)
		image = cv2.resize(image,(177,177))
		cv2.imwrite(files[i],image)