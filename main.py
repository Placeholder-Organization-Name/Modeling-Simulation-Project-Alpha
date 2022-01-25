import os

os.system("python3 writeSystem.py") #Necessary for generating initialConditions.txt file
os.system("./nbody < initialConditions.txt")
os.system("python3 graphOrbit.py")
