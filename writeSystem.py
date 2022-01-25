import chooseBodies
import regex as re
import sys
import requests
import os


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def getNameMassPosVel(file_name):
	bodyData = {}
	lines = open(file_name, 'r').readlines()
	bodyData['name'] = lines[4].split()[4]
	#print(lines[8])

	# GETTING MASS VALUE
	r = re.compile(".*Mass")#x10^\d* (\w*)")
	newlist = list(filter(r.match, lines))
	massLine = newlist[0].replace(" ","")
	massLine = massLine.replace(",","")
	massLine = re.findall("Mass.*10\^\d*\(*\w*\)*=~*\d*\.*\d*",massLine)[0]
	massUnit = re.findall("[^\d\(]*g",massLine)[0]
	massExp = int(re.findall("10\^\d*",massLine)[0][-2:])
	massValue = float(re.findall("\d*\.*\d*$",massLine)[0])

	realMassValue = massValue*(10**massExp)

	if(massUnit == 'g'):
		realMassValue /= 1000

	## GETTING POSITION [X,Y,Z]
	prevVecLine = [i for i, item in enumerate(lines) if re.search('\$\$SOE', item)][0]
	#print(lines[prevVecLine])
	coordLine = lines[prevVecLine+1].split()
	#print(coordLine)
	position = [float(coordLine[i][:-1]) for i in [4,5,6]]
	
	## GETTING VELOCITY [Vx, Vy, Vz]
	velocity = [float(coordLine[i][:-1]) for i in [7,8,9]]


	bodyData['mass'] = realMassValue
	bodyData['pos'] = position
	bodyData['velocity'] = velocity
		
	#print(bodyData)
	return bodyData


# NUMBER OF BODIES
# MASS (BODY 1)
# X (BODY 1)
# Y (BODY 1)
# Z (B1)
# Vx (B1)
# Vy (B1)
# Vz (B1)
#...

system = chooseBodies.returnSystem()
lines = [len(system)]
for body in system:
	### ASSIGN INPUT FILE FOR THE API
	replace_line('my_input_file.txt', 2, f"COMMAND={body}\n")
	
	### EXTRACT THE REQUIRED DATA FROM THE API USING SAID FILE
	os.system(f'python3 horizonsAPI.py my_input_file.txt > results_{body}.txt')

	### GET THE NAME, MASS, POSITION, AND VELOCITY FROM THE CORRESPONDING BODY
	bodyData = getNameMassPosVel(f'results_{body}.txt')
	lines.append(bodyData["name"])
	lines.append(bodyData['mass'])
	for i in range(3):
		lines.append(bodyData['pos'][i])

	for i in range(3):
		lines.append(bodyData['velocity'][i])


with open('initialConditions.txt', 'w') as f:
	for line in lines:
		f.write(str(line))
		f.write("\n")
