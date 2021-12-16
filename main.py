import sys
import re

def Sqrtt(number):

	start = 0
	precision = 8
	end, ans = number, 1
	while (start <= end):
		mid = int((start + end) / 2)

		if (mid * mid == number):
			ans = mid
			break
		if (mid * mid < number):
			start = mid + 1
			ans = mid
		else:
			end = mid - 1

	increment = 0.1
	for i in range(0, precision):
		while (ans * ans <= number):
			ans += increment

		ans = ans - increment
		increment = increment / 10

	return ans

def Sqrt(n):

		x = n
		y = 1

		# e decides the accuracy level
		e = 0.00000001
		while(x - y > e):

			x = (x + y)/2
			y = n / x

		return x

def Sqrt_what(n):
	return n ** (1/2)

def SolveEquation(a, b, c):
	if (a == 0 and b == 0):
		print("Any number in R is a solution")
	elif (a == 0):
		print("1 solution: X = " , (-c) / b)
	else:
		delta = b * b - 4 * a * c
		if (delta == 0):
			print("1 solution: X = " , (-b) / (2 * a))
		elif (delta > 0):
			print("two real solutions:")
			print("X1 = ", (-b + Sqrt(delta)) / (2 * a))
			print("X2 = ", (-b - Sqrt(delta)) / (2 * a))
		else:
			print("two Im solutions:")
			print("X1 = ", (-b) / (2 * a), " i", Sqrt(delta)/(2 * a))
			print("X2 = ", (-b) / (2 * a), " i", Sqrt(delta)/(2 * a))

if (len(sys.argv) != 2):
	print("python3 computerv1 [equation]")
	print("euation eg: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
	exit()

print("equation: " + sys.argv[1] + "\n-------------------------")
str = sys.argv[1].split(' ')
print(str)
pairs = [(0, 0), (1, 1), (2, 0)] # pars: (power, coefecion)
signe = 1
print("pairs: ", pairs)
#for x in str:

