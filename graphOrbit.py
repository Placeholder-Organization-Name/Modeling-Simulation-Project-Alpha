import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

file1= open('example.txt')
count = 0

l = file1.readline().split("\t")
count += 1
M = int(l[0])
N = int(l[1])

particles = []
names = []
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

for i in range(M):
	names.append(file1.readline())

fig = plt.figure()
ax = fig.gca(projection='3d')
#ax = fig.add_subplot(projection='3d')

for i in range(M):
	ax.plot(particles[i][0], particles[i][1],particles[i][2] , label=names[i])
#ax.plot(particles[1][0], particles[1][1],particles[1][2] , label='parametric curve')

def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])

ax.scatter(0,0,0,label = 'center')
plt.legend()
#ani = animation.FuncAnimation(fig, update, 100, fargs=(particles, line), interval=10000/100, blit=False)
plt.show()
