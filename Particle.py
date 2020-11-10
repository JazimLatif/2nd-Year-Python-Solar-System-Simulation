import math
import numpy as np
class Particle:
    '''Used to input particles to our solar system, with format of arrays for Position, Velocity and Acceleration, and associated mass and particle name.
    -----------
    Syntax
    
    Planetname(array for initial position, array for velocity, array for acceleration, name of particle, mass of particle)
    These are currently stored in the simulation file 
    The Particle Class's functions are called in NbodySystem class inside the simulate function to determine acceleration for each particle
    
    '''
    G=6.67408E-11
    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,-10,0], dtype=float), Name='Ball', Mass=1.0):
        self.position = np.array(Position)
        self.velocity = np.array(Velocity)
        self.acceleration = np.array(Acceleration)
        self.Name = Name
        self.mass = Mass
    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration)
    def update(self, deltaT):
        self.position = self.position + self.velocity*deltaT
        self.velocity = self.velocity + self.acceleration*deltaT

    def KineticEnergy(self):
        KineticEnergy = 0.5*self.mass* np.linalg.norm(self.velocity)**2
        return KineticEnergy
        #This function is used in simulation file to determine Ek of each planet
        #we will then use this Ek to sum the total for all the planets and plot it on a graph against time in our analysis file             
    def Momentum(self):
        Momentum = self.mass*self.velocity
        return Momentum
        #We do the same as Ek with Momentum on our graph


