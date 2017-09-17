#!/usr/bin/env python 

import random, sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from math import sqrt


inside = 0
piresults = {}
errorsize = {}
pi = np.pi
points = []

print ("\n" * 20)
print("****Welcome to Monte Carlo PI Simulator***")
print("Note: Simulating less than 1000 points will show a Cartesian Coordinate System with their locations.")
print("\n")

while True:
    try:
        total = int(input("How many points to generate: "))
    except ValueError:
        print("Sorry that's not a number.")
        continue
    if total == 0:
        print("Please try again with a number different from 0")
        continue

    if 10**7 <= total < 10**9:
        print("That may take a while!!!")
    elif total >= 10**9:
        print("Try with a smaller number of points")
        continue
    break

def set_window_geometry(x, y, z, k):
    mvr = plt.get_current_fig_manager()
    mvr.window.setGeometry(x, y, z, k)

if total<=10**3:
    plt.figure("Distribution") 
    plt.title("Point distribution")
    set_window_geometry(800, 0, 700, 700)
    ax = plt.axes()
    ax.set_aspect(1)
    theta = np.linspace(-np.pi, np.pi, 200)
    plt.plot(np.sin(theta), np.cos(theta))
    plt.show(block=False)

def check_if_inside(x,y):
    if sqrt(x*x + y*y)<=1:
        return 1
    else:
        return 0

def estimate_pi(inside,total):
    return 4*inside/total

for i in range(1,total+1):
     x = random.uniform(-1, 1)
     y = random.uniform(-1, 1)
     inside += check_if_inside(x,y)
     points.append([x,y])
     
     if total<=10**3:
        plt.plot(x,y, 'or')
     
     if i<= 100 or i%(10**2) == 0:
         piest = estimate_pi(inside,i)
         piresults[i] = piest
         errorsize[i] = abs(pi-piest)
     if i%(2*(10**6)) == 0:
         print("Reached point %s"% i)

        
print("The final calculation for PI is:%s"%estimate_pi(inside,total))
print("The average calculated PI is %s"%(sum(piresults.values())/len(piresults)))

plt.figure("Absolute Difference")
plt.plot(list(errorsize.keys()), list(errorsize.values()))
mngr = plt.get_current_fig_manager()
set_window_geometry(0, 0, 700, 700)
plt.title("Abs difference from true PI")
plt.xlabel("Points")
plt.ylabel("Diff")
plt.show()

sys.exit()