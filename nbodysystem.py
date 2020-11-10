import numpy as np
from Particle import Particle
import math
import copy
G=6.67408E-20


class nBodySystem:
    '''
    '''
    def __init__(self, listofplanets,Potential):
        self.listofplanets = np.array(listofplanets)
        self.Potential = Potential
        #The array of list of planets contains all the planets our simulation is going to run
        #The potential is a scalar so we can assign it a simple variable called potential
    def __repr__(self):
        result = ""
        for planet in self.listofplanets:
            result += f"{str(planet)}\n"
        return result

    def simulate(self):
        delta = 10000
        for planet1 in self.listofplanets:
            totalAcc = np.array([0,0,0])
            for planet2 in self.listofplanets:
                if planet1 != planet2:
                    separationOfBodies = planet1.position - planet2.position
                    Magnitude = np.linalg.norm(separationOfBodies)
                    totalAcc = totalAcc - separationOfBodies*(G*planet2.mass/Magnitude**3)
            planet1.acceleration = totalAcc
        for planet in self.listofplanets:
            planet.update(delta)        
    #This is the main function in our code which we use to simulate planet acceleration
    #The loop counts through every planet and adjusts the position based on the acceleration and formulas in the update function in particle
    #There is a check so that the planet does not adjust if it is compared against itself on line 25

    def PE(self):
        delta = 1
        for planet1 in self.listofplanets:
            Potential = 0
            for planet2 in self.listofplanets:
                if planet1 != planet2:
                    separationOfBodies = planet1.position - planet2.position
                    Magnitude = np.linalg.norm(separationOfBodies)
                    self.Potential -= G*planet1.mass*planet2.mass/Magnitude
            Potential += self.Potential
    #This is the forumla for potential, I cannot figure out how to get it to calculate our system yet.