import numpy as np
from Particle import Particle
import math
import copy
from nbodysystem import nBodySystem


sunMass = 1.989e30
Sun = Particle(np.array([-5.331384946352059E+05 , 1.120717181372234E+06 , 2.476857077049906E+03]), np.array([-1.457356265786345E-02, -2.928417920324491E-03 , 4.012213052299406E-04]), np.array([0,0,0]),'Sun', sunMass)

mercuryMass = 3.285e23 
Mercury = Particle(np.array([5.809171111230399E+06,4.660809324124105E+07,3.138678328370906E+06]),np.array([-5.803594514327065E+01,8.497172476510618E+00,6.017560202959968E+00]), np.array([0,0,0]),'Mercury', mercuryMass)

venusMass = 4.867e24
Venus = Particle(np.array([4.174231210320611E+07,-9.916972093263733E+07 ,-3.812647412093356E+06]), np.array([3.202363506379974E+01 , 1.347662520863154E+01 ,-1.663483609630161E+00]), np.array([0,0,0]),'Venus', venusMass)

earthMass = 5.972e24
Earth = Particle(np.array([4.686168531508415E+07, 1.407536286305435E+08 , -3.659104520827532E+03]), np.array([-2.871320759741131E+01 , 9.449091487355650E+00 , 5.947952778142529E-04]), np.array([0,0,0]),'Earth', earthMass)

moonMass = 7.348e22
Moon = Particle(np.array([4.723488711341201E+07 , 1.406034476926991E+08 ,-3.543903024609387E+04]), np.array([-2.833906625132419E+01 , 1.034057959556280E+01 ,-4.536824715365562E-02]), np.array([0,0,0]),'Moon', moonMass)

marsMass = 6.390e23
Mars = Particle(np.array([-2.385506107529634E+08 ,-5.339151128544627E+07 , 4.699980374694895E+06]), np.array([6.297541610269952E+00 ,-2.154887905915407E+01 ,-6.059698671362570E-01]), np.array([0,0,0]),'Mars', marsMass)

jupiterMass = 1.898e27
Jupiter = Particle(np.array([2.808912063774594E+07 ,-7.828230391310869E+08 , 2.618156246833920E+06]), np.array([1.289915801971427E+01 , 1.092151448518059E+00 ,-2.930202471875685E-01]), np.array([0,0,0]),'Jupiter', jupiterMass)

saturnMass = 5.683e26
Saturn = Particle(np.array([5.346414997964485E+08 ,-1.402052100316806E+09 ,3.095017390286267E+06]), np.array([8.489881246744599E+00 , 3.413887646181087E+00 ,-3.976903143060998E-01]), np.array([0,0,0]),'Saturn', saturnMass)

uranusMass = 8.681e25
Uranus = Particle(np.array([2.442044135127703E+09 , 1.682889730267486E+09,-2.538669917408276E+07]), np.array([-3.914255057058745E+00 , 5.290072668841669E+00 , 7.040713784524910E-02]), np.array([0,0,0]),'Uranus', uranusMass)

neptuneMass =1.024e26
Neptune = Particle(np.array([4.369694004295476E+09 ,-9.721695441997778E+08 ,-8.068399610952908E+07]), np.array([1.143871624768453E+00 , 5.338246708527643E+00 ,-1.355876349112393E-01]), np.array([0,0,0]),'Neptune', neptuneMass)

plutoMass = 1.309e22
Pluto = Particle(np.array([1.920697791827656E+09 ,-4.695341600789963E+09 ,-5.315082251251578E+07]), np.array([5.142626115848500E+00 , 9.036984385318513E-01 ,-1.565642507189335E+00]), np.array([0,0,0]),'Pluto', plutoMass)

testMass = 1
Test = Particle(np.array([6371,0,0]), np.array([0,0,0]), np.array([0,0,0]),'Test', testMass)

masslessMass = 0
Massless = Particle(np.array([6371,0,0]), np.array([0,0,0]), np.array([0,0,0]),'Massless', masslessMass)

nearlyMasslessMass=0.00001
NearlyMasslessMass = Massless = Particle(np.array([6371,0,0]), np.array([0,0,0]), np.array([0,0,0]),'Massless', nearlyMasslessMass)

testEarthMass = 5.972e24
TestEarth = Particle(np.array([0,0,0]), np.array([0,0,0]), np.array([0,0,0]),'TestEarth', testEarthMass)
'''
These are the planetary data values I inputted from JPL Horizons Ephemeris page, the synax is assigned in the Particle class file.
the test Particles are used for testing in my analysis, the rest of the data values include the sun, 8 planets, our moon Luna and pluto. 
For the purpose of the simulation I ignored pluto, however to include it, all we have to do it add pluto to the list called listofplanets below
to run the tests I commented the full list out of the simulation and ran the shorter listofplanets including the test particles below.
'''
listofplanets= [Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune]
#listofplanets= [TestEarth, nearlyMasslessMass]


Potential = 0

Solarsystem= nBodySystem(listofplanets,Potential)
#This uses our nbodysystem code to run the class nBodySystem on the listofplanets and our Potential, I cannot get the potential to work to obtain the Total Energy of the system using the Virial Theorem


print(Solarsystem)

data=[]
time=0

for i in range(200000):
    Solarsystem.simulate()
    TotalKineticEnergy = 0
    Momentum = 0
    for planet in listofplanets:
            TotalKineticEnergy += planet.KineticEnergy()
            Momentum += planet.Momentum()
            TotalEnergy = 2*(TotalKineticEnergy)-Potential #Attempt at using The Virial Theorem, cannot figure out how to get potential to work
    if (i%100==0):        
        item = [time,copy.deepcopy(Solarsystem),copy.deepcopy(TotalKineticEnergy),copy.deepcopy(Momentum)]
        data.append(item)
    time += 60*60    
np.save("saveData",data,allow_pickle=True)
print(Solarsystem)

#This is the code that simulates our solar system for the step count listed in range(n)
#The solar system is simulated for each value of the step count 
#The for loop obtains the values for Total Kinetic Energy and Momentum using the KineticEnergy and Momentum functions in Particle class
#The if loop saves our values every 100 steps to a list called data which is saved in the file saveData to be read back from in the analysis file.
#The code prints solar system initially and after running for the range given.