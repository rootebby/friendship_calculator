score = 0
while  True:
	
	names = input("enter names of 2 people : ")

	for char in names:
		if char in "aeiou":
			score += 5

		if char in "friend":
			score += 10

	print('your friendship score is:',score)

	if score > 100:
		score = 0
		names = input("enter names of 2 people : ")

	for char in names:
		if char in "aeiou":
			score += 5

		if char in "friend":
			score += 10
	print('your friendship score is:',score)

	if score > 100:
		print("best friends !")


