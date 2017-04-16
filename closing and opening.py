# 匯入library
import numpy as np
from PIL import Image
import random
import pylab as pl
import math
import pylab as pl
from collections import defaultdict

# 匯入圖片
im = Image.open('origin.png')

#設一些初始參數
size = im.size
output = Image.new("L", im.size, color=255)
mask = 3
element = np.array([[0,1,0], [1,1,1], [0,1,0]])
num = 5
pix = (np.array(im)).T
out = (np.array(im)).T

# 設計dilation函數
def dilation(i,j):
	global pix
	global out
	e = pix[i-1:i+2,j-1:j+2] * element
	if(e.any()):
		out[i,j] = 255
# 設計erosion函數
def erosion(i,j):
	global pix
	global out
	e = pix[i-1:i+2,j-1:j+2] * element
	s = np.sum(e)
	if(s / 255 > 0 and s / 255 < num):
		out[i,j] = 0

# closing
for k in range(26):
	for i in range(0+1,size[0]-1):
		for j in range(0+1,size[1]-1):
			if(pix[i,j] == 0):
				dilation(i,j)
	pix = np.copy(out)

for  i in range(size[0]):
	out[0,i] = 255
	out[599,i] = 255
	out[i,0] = 255
	out[i,599] = 255

pix = np.copy(out)
for k in range(26):
	for i in range(0+1,size[0]-1):
		for j in range(0+1,size[1]-1):
			if(pix[i,j] == 255):
				erosion(i,j)
	pix = np.copy(out)



# opening
pix = np.copy(out)
for k in range(57):
	for i in range(0+1,size[0]-1):
		for j in range(0+1,size[1]-1):
			if(pix[i,j] == 255):
				erosion(i,j)
	pix = np.copy(out)

for  i in range(size[0]):
	out[0,i] = 0
	out[599,i] = 0
	out[i,0] = 0
	out[i,599] = 0

pix = np.copy(out)
for k in range(48):
	for i in range(0+1,size[0]-1):
		for j in range(0+1,size[1]-1):
			if(pix[i,j] == 0):
				dilation(i,j)
	pix = np.copy(out)

# 輸出結果
output = Image.fromarray(out.T)
output.show()
output.save("temp.png")