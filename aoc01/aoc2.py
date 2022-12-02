# Function to convert calories in str to int

def to_int(li):
	return_list = []
	for element in li:
		if element == "":
			pass
		else:
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

calorie_list.sort(reverse=True)

top_three = [calorie_list[0], calorie_list[1], calorie_list[2]]

print(sum(top_three))

