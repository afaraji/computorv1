import sys

pairs = [(0, 0), (1, 1), (2, 0)] # pars: (power, coefficient)

def is_power_in_list(power):
	for i in range(len(pairs)):
		if pairs[i][0] == power:
			return i
	return -1

def sort_by_power(e):
	return e[0]

def Add_pair(power, coefficient):
	position = is_power_in_list(power)
	if (position < 0):
		pairs.insert(position, (power,coefficient))
		pairs.sort(key=sort_by_power)
	else:
		pairs[position][1] += coefficient

def Validate_list():
	for x in pairs[:]:
		if (x[0] > 2 or x[0] < 0):
			if x[1] == 0:
				pairs.remove(x)
			else:
				print("Error: Only polynomial second or lower degree equation are allowed.")
				return False
	a = pairs[2][1]
	b = pairs[1][1]
	c = pairs[0][1]
	print("Reduced form:", c,"* X^0", b,"* X^1", a,"* X^2 = 0")
	print("(", a, "X^2",b, "X", c, "= 0)")
	SolveEquation(a, b, c)

def Sqrt(n):
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
			print("X1 =", (-b) / (2 * a), "+", Sqrt(-delta)/(2 * a), "i")
			print("X2 =", (-b) / (2 * a), "-", Sqrt(-delta)/(2 * a), "i")

if (len(sys.argv) != 2):
	print("python3 computerv1 [equation]")
	print("euation eg: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
	exit()

def Parser(text):
	text.replace(" ", "")

print("equation: " + sys.argv[1] + "\n-------------------------")
str = sys.argv[1].split(' ')
a = str[0]
b = str[1]
c = str[2]
SolveEquation(float(a), float(b), float(c))
exit()
print(str)

signe = 1
print("pairs: ", pairs)
#for x in str:

############# Grammar #############

# simple_equation  : signe term '=' simple_equation
#                  | term '=' simple_equation
#                  | signe term operend simple_equation '=' simple_equation
#                  | term operend simple_equation '=' simple_equation
#                  | cmd_name cmd_suffix
#                  | cmd_name
#                  ;
# term             :
#                  ;
# cmd_word         : WORD
#                  ;
# cmd_prefix       :            io_redirect
#                  | cmd_prefix io_redirect
#                  |            ASSIGNMENT_WORD
#                  | cmd_prefix ASSIGNMENT_WORD
#                  ;
# cmd_suffix       :            io_redirect
#                  | cmd_suffix io_redirect
#                  |            WORD
#                  | cmd_suffix WORD
#                  ;
# redirect_list    :               io_redirect
#                  | redirect_list io_redirect
#                  ;
# io_redirect      :           io_file
#                  | IO_NUMBER io_file
#                  |           io_here
#                  | IO_NUMBER io_here
#                  ;
# io_file          : '<'       filename
#                  | LESSAND   filename
#                  | '>'       filename
#                  | GREATAND  filename
#                  | DGREAT    filename
#                  | LESSGREAT filename



# def Sqrt_old(number):

# 	start = 0
# 	precision = 8
# 	end, ans = number, 1
# 	while (start <= end):
# 		mid = int((start + end) / 2)
# 		if (mid * mid == number):
# 			ans = mid
# 			break
# 		if (mid * mid < number):
# 			start = mid + 1
# 			ans = mid
# 		else:
# 			end = mid - 1

# 	increment = 0.1
# 	for i in range(0, precision):
# 		while (ans * ans <= number):
# 			ans += increment

# 		ans = ans - increment
# 		increment = increment / 10

# 	return ans
