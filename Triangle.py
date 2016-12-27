import sys

print(sys.platform)

num = int(input('input a number ...> '))

for row in range(num):
	print(' '*(num-row-1)+'* '*(row+1))

for row in range(num-1):
	print(' '*(row+1)+'* '*(num-row-1))