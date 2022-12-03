lower_priority_dict = {chr(i):(i-96) for i in range(97, 123)}

upper_priority_dict = {chr(i):(i-38) for i in range(65, 91)}


total_priority = 0


# Function to split the items jn equal lengths

def spl(string):
	length = int(len(string))
	
	splitted_list = []
	first_item = "".join(list(string)[0:int(length/2)])
	
	second_item = "".join(list(string)[int(length/2):length])
	
	splitted_list = [first_item, second_item]
	
	return splitted_list
	
# Function to check which item is same in both the compartments

def same_item(p1, p2):
	for i in p1:
		if i in p2:
			return i
		
		else:
			pass

main_list = [spl(x) for x in your_input.split("\n")]
del main_list[0], main_list[-1]


for item in main_list:
	first = item[0]
	second = item[1]

	same = same_item(first, second)
	if same.islower():
		total_priority += lower_priority_dict[same]

	else:
		total_priority += upper_priority_dict[same]
		
print(total_priority)


