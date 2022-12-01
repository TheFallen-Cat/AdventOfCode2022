# Function to convert the elements inside a list from str to int

def to_int(li):
	return_list = []
	for element in li:
		return_list.append(int(element))
		
	return return_list
	
# Function to check the highest calorie in the calorie_list

def greatest(li):
	highest = 0
	
	for element in li:
		if element >= highest:
			highest = element
		else:
			pass
			
	return highest


main_list = your_input.split("\n\n")

new_list = []

for i in main_list:
	
	splitted = i.split("\n")

	new_list.append(to_int(splitted))
	
calorie_list = []

for elf, calorie in enumerate(new_list):
	calorie_list.append(sum(calorie))

	
print(greatest(calorie_list))
