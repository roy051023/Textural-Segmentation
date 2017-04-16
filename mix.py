# 匯入library
import numpy as np
from PIL import Image
import random
import pylab as pl
import math
import pylab as pl
from collections import defaultdict

im = Image.open('temp.png')
im2 = Image.open('origin.png')

size = im.size
temp = Image.new("L", size)
maskSize = 3

out = (np.array(im)).T

for i in range(size[0]):
	out[0,i] = out[1,i]
	out[599,i] = out[598,i]
	out[i,0] = out[i,1]
	out[i,599] = out[i,598]

im = Image.fromarray(out.T)


# 一階微分
for i in range(0 + int(maskSize / 2), size[0] - int(maskSize / 2)):
	for j in range(0 + int(maskSize / 2), size[1] - int(maskSize / 2)):
		first = abs((im.getpixel((i-1,j+1)) + 2*im.getpixel((i,j+1)) + im.getpixel((i+1,j+1))) - (im.getpixel((i-1,j-1)) + 2*im.getpixel((i,j-1)) + im.getpixel((i+1,j-1)))) + abs((im.getpixel((i+1,j-1)) + 2*im.getpixel((i+1,j)) + im.getpixel((i+1,j+1))) - (im.getpixel((i-1,j-1)) + 2*im.getpixel((i-1,j)) + im.getpixel((i-1,j+1))))
		temp.putpixel((i,j),first)

# 合併兩張圖
for i in range(size[0]):
	for j in range(size[1]):
		if(temp.getpixel((i,j)) > 30):
			im2.putpixel((i,j), 100)

im2.save("result.png")