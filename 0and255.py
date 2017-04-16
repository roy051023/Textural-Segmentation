# 匯入library
import numpy as np
from PIL import Image
import random
import pylab as pl
import math
import pylab as pl
from collections import defaultdict

# 因為老師的圖很多雜訊，所以我圖片二值化，方便處理
im = Image.open('HW5.tif').convert('L')

size = im.size
output = Image.new("L", im.size)

for i in range(size[0]):
	for j in range(size[1]):
		if(im.getpixel((i,j)) > 80):
			output.putpixel((i,j), 255)
		else:
			output.putpixel((i,j), 0)

output.save("origin.png")