import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

file1= open('example.txt')
count = 0

l = file1.readline().split("\t")
count += 1
M = int(l[0])
N = int(l[1])

particles = []
print(M)
for i in range(M):
	particles.append([[],[],[]]) #[x,y,z]

print(particles)
for i in range(N):
	for particle in range(M):
		line = file1.readline()
		l = line.split("\t")
		
		particles[particle][0].append(float(l[0])) #x
		particles[particle][1].append(float(l[1])) #y
		particles[particle][2].append(float(l[2])) #z

#for p in particles:
#	print(p)

fig = plt.figure()


fig = plt.figure()

ax = fig.gca(projection='3d')
ax.scatter(0,0,0,label = 'center')
ax.plot(particles[0][0], particles[0][1],particles[0][2] , label='parametric curve')
ax.plot(particles[1][0], particles[1][1],particles[1][2] , label='parametric curve')

plt.legend()
plt.show()
