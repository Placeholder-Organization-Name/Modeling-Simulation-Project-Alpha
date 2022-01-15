import math
import random
import numpy as np

G = 6.67e-11 # Nm2/kg2

class particle():
    mass = 1.0 #kg
    r = np.array([0.0, 0.0, 0.0]) #m
    F0 = np.array([0.0,0.0,0.0])
    
    def __init__(self, m, p, v):
        self.mass = np.array(m)
        self.pos = np.array(p)
        self.vel = np.array(v)

    def print_position(self):
        print(self.pos[0],"\t",self.pos[1],"\t",self.pos[2])

    def u(self,p_j):
        self.r = p_j.pos - self.pos
        return self.r
    
class container():
    particles = []
    def __init__(self, particles):
        self.particles = particles
        
    def print_position(self):
        for particle in self.particles:
            particle.print_position()
        
class integrator():
    t0 = 0.0
    dt = 0.01 #sec
    steps = 1
    M=0
    def __init__(self, t0, dt, steps, M):
        self.t0 = t0
        self.dt = dt
        self.steps = steps
        self.M = M

    def riemman(self, container):
        for j in range(self.M):
            p_j = container.particles[j]            
            for i in range(self.M):
                p_i = container.particles[i]
                if (i == j):
                    continue
                
                u = p_j.u(p_i)
                r = np.linalg.norm(u)
                C = (G*p_j.mass * p_i.mass / (r**3))
                F = C*u
                V = (self.dt/p_j.mass)*F
                p_j.vel = p_j.vel + V

        # 2 on the spot        
        for j in range(self.M):
            p_j = container.particles[j]            
            #v=d/t
            # d = vt
            p_j.pos = p_j.pos + p_j.vel * self.dt

        return container
                
dt = 1e-1
M = 2 #num particulas
N = 100 #iteraciones

p0 = particle(1, [0,0,0], [0,0,0]) #particula0 en el origen y reposo
p1 = particle(1, [0.001,0,0], [0.0,0,0]) #particula1 en el x= 1 origen y reposo

#metemos particulas al contenedor

c1 = container([p0,p1])

#resolver el sistema dentro del contenedor o pasar a resolvedor**creamos integrador

s1 = integrator(0.0, dt, 1, M) #integra cada y da respuesta cada...

print(M, N) #Num particulas, num iteraciones

for i in range (5):
    c1 = s1.riemman(c1) #lo integramos y pasamos el contenedor// regresa contenedor ya actualizado
    c1.print_position()
