import sys

number = int(sys.argv[1])

for i in rang(1,number+1):
	if number % i == 0:
		print(i,end=" ")

print()
