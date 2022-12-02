# Function to check who won and return the won points

def who_won(li):
	
	opponent = li[0]
	you = li[1]
	
	your_score = 0
	
	points = {"X" : 1, "Y": 2, "Z": 3}
	
	# Winning Conditions
	
	if opponent == "A" and you == "Y":
		your_score += 6 + points[you]
		
	elif opponent == "B" and you == "Z":
		your_score += 6 + points[you]
		
	elif opponent == "C" and you == "X":
		your_score += 6 + points[you]
		
	# Draw Conditions
	
	elif opponent == "A" and you == "X":
		your_score += 3 + points[you]
		
	elif opponent == "B" and you == "Y":
		your_score += 3 + points[you]
		
	elif opponent == "C" and you == "Z":
		your_score += 3 + points[you]
	
	# Lost Conditions
	
	elif opponent == "A" and you == "Z":
		your_score += 0 + points[you]
		
	elif opponent == "B" and you == "X":
		your_score += 0 + points[you]
		
	elif opponent == "C" and you == "Y":
		your_score += 0 + points[you]
		
		
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

