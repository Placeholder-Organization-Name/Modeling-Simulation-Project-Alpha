### SCRIPT TO CHOOSE SOLAR SYSTEM'S BODIES ###

def printInstructions(inst):
	instText = ""
	if(inst == '0'):
		instText = "Choose any of the following options:\n* 1: Predefined system of bodies\n* 2: Custom system of bodies\n* Consider that for this code, we're always considering the Sun as the center of the X, Y and Z planes."
	elif(inst == '1'):
		instText = "Choose one of the following systems:\n* 1: Sun-Earth\n* 2: Solar-System"
	elif(inst == '2'):
		instText = "Input the number id of the bodies you're going to simulate.\nWhen finished type 'done'\nSome id examples are:\n* Sun: 10\n* Mercury: 199\n* Venus: 299\n* Earth: 399\n* Mars: 499\n* Jupiter: 599\n* Saturn: 699\n* Uranus: 799\n* Neptune: 899\nFor more ids, you can consult the Horizon's webpage https://ssd.jpl.nasa.gov/horizons/app.html#/"
	
	print(instText)

def customSystems():
	while(True):
		option = input("Option: ")
		if(option == '1'):
			return [10,399]
		elif(option == '2'):
			return [10,199,299,399,499,599,699,799,899]

def createSystem():
	universe = []
	while(True):
		body = input("ID: ")
		if(body not in universe and body.isnumeric()):
			universe.append(body)
		elif(body == "done"):
			return universe
def chooseOption1():
	option = ''
	while(True):
		option = input("Option: ")
		if(option == '1'):
			printInstructions(option)
			return customSystems()
		elif(option == '2'):
			printInstructions(option)
			return createSystem()

def returnSystem():
	printInstructions('0')
	return chooseOption1()
