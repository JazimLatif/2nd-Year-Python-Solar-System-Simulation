import numpy as np
from Particle import Particle
import math
import copy
from nbodysystem import nBodySystem
from matplotlib import pyplot as plt


Data = np.load("saveData.npy",allow_pickle = True)
def findPosition(Data,index):
    positions=[]
    for i in Data:
        positions.append(i[1].listofplanets[index].position)
    return np.array(positions)
#This loads the data from our simulation file, and calculates the positions of our planets using the method above
#We will use this method to append the positions of planets to a plottable list


positions = []
i=0


for i in range(len(Data[0][1].listofplanets)):
    positions.append(findPosition(Data,i))
for i in range(len(Data[0][1].listofplanets)):
    plt.plot(positions[i][:,0],positions[i][:,1])
    plt.axis('equal')
plt.title("Positions of planets (Bird's Eye View)")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig('PositionGraph.jpg')
plt.show()
#This takes the X and Y values (the zeroth and first items in our list of velocity data)
#And plots them on an X and Y axis giving us the orbits of the system


KE=[]
time=[]

for i in range(len(Data)):
    KE.append(Data[i][2])
    time.append(Data[i][0])


plt.plot(time,KE)
plt.title("Kinetic Energy of system as a funtion of Time")
plt.xlabel("Time")
plt.ylabel("Kinetic Energy")
plt.savefig('KEGraph.jpg')
plt.show()

#This is a simpler method due to Kinetic Energy being a scalar quantity
#It takes the first (time) and 3rd (Kinetic Energy) value from our saved data list and plots them to an axis


momentum=[]

for i in range(len(Data)):
    momentum.append(Data[i][3])
plt.plot(time,momentum)
plt.title("Momentum as a function of Time")
plt.xlabel("Time")
plt.ylabel("Momentum")
plt.savefig('MomentumGraph.jpg')
plt.show()

#Momentum is also scalar, so similarly to Ek, we can take time and Kinetic energy of each particle and plot them onto a graph


