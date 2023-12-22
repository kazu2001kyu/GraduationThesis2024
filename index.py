import csv
import colorsys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import random

# for i in range(1000):
#     print(colorsys.rgb_to_hsv(random.random(), random.random(), random.random()))

file_name ="data/data3333halo.csv"

H = []
S = []
V = []
max_size = 5

with open(file_name, encoding='utf8') as f:
    reader = csv.reader(f)
    header = next(reader)
    h = []
    s = []
    v = []
    c = 1
    for row in reader:

        r = int(row[1])
        g = int(row[2])
        b = int(row[3])
        hsv = colorsys.rgb_to_hsv(r/255,g/255,b/255)
        h.append(hsv[0])
        s.append(hsv[1])
        v.append(hsv[2])
        if int(row[0]) != c:
            c += 1
            H.append(h)
            S.append(s)
            V.append(v)
            if c < max_size+1:
                h = []
                s = []
                v = []

# PYTHON_MATPLOTLIB_3D_PLOT_02
H.append(h)
S.append(s)
V.append(v)

# Figureを追加
fig = plt.figure()

# 3DAxesを追加
ax = fig.add_subplot(projection='3d')

# Axesのタイトルを設定
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(0,1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Value")

size = 5
for j in range(0,1):
    x = []
    y = []
    z = V[j]
    for i in range(len(S[j])):
        x.append(S[j][i]*math.cos(2*math.pi*H[j][i]))
        y.append(S[j][i]*math.sin(2*math.pi*H[j][i]))
    color = "r"
    if j == 0:
        color = "b"
    if j == 1:
        color = "0.6"
    if j == 2:
        color = "g"
    if j == 3:
        color = "y"
    if j == 4:
        color = "c"
    if j == 5:
        color = 'k'
    if j == 6 :
        color = 'm'  
    if j == 8:
        color = "b"
    if j == 9:
        color = "0.6"
    if j == 10:
        color = "g"
    if j == 11:
        color = "y"
    if j == 12:
        color = "c"
    if j == 13:
        color = 'k'
    if j == 14:
        color = 'm'  
    if j == 16:
        color = "b"
    if j == 17:
        color = "0.6"
 
    ax.scatter(x, y, z, s=0.1, label=str(j+3)+"枚の場合", c=color)
    

ax.legend()
plt.show()