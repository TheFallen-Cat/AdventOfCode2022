# Function to check the common item in amomg all the 3 items

def same_item(l):
	first = l[0]
	second = l[1]
	third = l[2]
	
	for letter in first:
		if letter in second:
			if letter in third:
				return letter
				
			else:
				pass
				
		else:
			pass
			

lower_priority_dict = {chr(i):(i-96) for i in range(97, 123)}

upper_priority_dict = {chr(i):(i-38) for i in range(65, 91)}

total_priority = 0

main_list = your_input.split("\n")
del main_list[0], main_list[-1]

grouped_list = []

x = 0

# To create a list with grouped pair of 3 items

for i in range(100):
	temp = main_list[x:x+3]
	grouped_list.append(temp)
	x += 3

	
for item in grouped_list:
	same = same_item(item)
	
	if same.islower():
		total_priority += lower_priority_dict[same]
		
	else:
		total_priority += upper_priority_dict[same]
		
print(total_priority)