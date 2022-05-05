# 3Danimate.py: 3-D animation of EM Wave
# Plots sin and cos waves perpendicular to each other

from vpython import *  # import graphics routines

xmax = 201  # number of x, y points
scene = canvas(x=0, y=0, width=500, height=500,
                title='sin(6pi*x/201-t)', background=(1., 1., 1.0),
                forward=(-0.6, -0.5, -1))
sinWave = curve(x=range(0, xmax), color=color.yellow, radius=4.5)
cosWave = curve(x=range(0, xmax), color=color.red, radius=4.5)
Xaxis   = curve(pos=[(-300, 0, 0), (300, 0, 0)], color=color.blue)
incr = math.pi/xmax

for t in arange(0, 10, 0.02):
    for i in range(0, xmax):
        x = i*incr
        f  = math.sin(6.0*x-t)
        zz = math.cos(6.0*x-t)
        yp = 100*f
        xp = 200*x-300
        zp = 100*zz
        sinWave.x[i] = xp
        sinWave.y[i] = yp
        cosWave.x[i] = xp
        cosWave.z[i] = zp


