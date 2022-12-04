def spl(l):
	
	return_list = []
	l = l.split(",")
	
	first = l[0].split("-")
	second = l[1].split("-")
	
	range1 = list(range(int(first[0]), int(first[1]) + 1))
	range2 = list(range(int(second[0]), int(second[1]) + 1))
	
	return_list.append(range1)
	return_list.append(range2)
	
	return return_list

	
main_list = [spl(x) for x in your_input.split("\n") if x != '']

sublists = 0

for i in main_list:
	
	list1 = i[0]
	list2 = i[1]
	
	if all(x in list1 for x in list2) or all(x in list2 for x in list1):
		sublists += 1
		
	else:
		pass
			
			
	
print(sublists)
