def HourMinute(num):
	if num < 60: 
		print("0:",num)
	else:
		hours = num/60
		mins = num%60
		print(int(hours),":",mins)
		

num = int(input("Enter the total number of minutes"))
HourMinute(num)
