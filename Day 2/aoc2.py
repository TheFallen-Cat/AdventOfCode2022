

# Function to check who won and return the won points

def who_won(li):
	
	opponent = li[0]
	you = li[1]
	
	your_score = 0
	
	

	if opponent == "A" and you == "X":
		your_score += 3
		
	elif opponent == "B" and you == "X":
		your_score += 1
		
	elif opponent == "C" and you == "X":
		your_score += 2
		
	
	elif opponent == "A" and you == "Y":
		your_score += 4
		
	elif opponent == "B" and you == "Y":
		your_score += 5
		
	elif opponent == "C" and you == "Y":
		your_score += 6
	
	
	elif opponent == "A" and you == "Z":
		your_score += 8
		
	elif opponent == "B" and you == "Z":
		your_score += 9
		
	elif opponent == "C" and you == "Z":
		your_score += 7

	return your_score
		
	
	
main_list = your_input.split("\n")

new_list = []

for i in main_list:
	splitted = i.split()
	
	if splitted == []:
		pass
	else:
		new_list.append(splitted)
	
	
points_list = []

for j in new_list:
	
	score = who_won(j)
	points_list.append(score)


print(sum(points_list))