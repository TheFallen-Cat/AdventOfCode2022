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
	
	for j in list1:
		if j in list2:
			sublists += 1
			break
		else:
			pass
			
			
	
print(sublists)