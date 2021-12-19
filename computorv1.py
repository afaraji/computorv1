import sys

SQUARE = "\u00B2" #unicode for ²
ESC = '\x1b'

pairs = [(0, 0), (1, 0), (2, 0)] # pars: (power, coefficient)

def Error(text, error_num = 1):
	print("\x1b[6;30;41mERROR:\x1b[0m", text)
	exit(error_num)

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
		pairs[position] = (pairs[position][0], pairs[position][1] + coefficient)

def Validate_list():
	for x in pairs[:]:
		if (x[0] > 2 or x[0] < 0):
			if x[1] == 0:
				pairs.remove(x)
			else:
				Error("Only polynomial second or lower degree equation are allowed.", 1)
	a = pairs[2][1]
	b = pairs[1][1]
	c = pairs[0][1]
	print("Reduced form:", c,"* X^0 +", b,"* X^1 +", a,"* X^2 = 0")
	print("(", a, "X" + SQUARE + " +",b, "X +", c, "= 0)")
	SolveEquation(a, b, c)

def Sqrt(n):
	return n ** (1/2)

def SolveEquation(a, b, c):
	if (a == 0 and b == 0):# what if c == 0
		if (c == 0): print("Any number in R is a solution.")
		else: print("No solution, Enter a valid Quadratic equation.")
	elif (a == 0):
		print("1 solution: X = " , (-c) / b)
	else:
		delta = b * b - 4 * a * c
		if (delta == 0):
			print("Discriminant is 0, 1 solution: X = " , (-b) / (2 * a))
		elif (delta > 0):
			print("Discriminant is strictly positive, two real solutions:")
			print("X1 = ", (-b + Sqrt(delta)) / (2 * a))
			print("X2 = ", (-b - Sqrt(delta)) / (2 * a))
		else:
			print("Discriminant is strictly negative, two Im solutions:")
			print("X1 =", (-b) / (2 * a), "+", Sqrt(-delta)/(2 * a), "i")
			print("X2 =", (-b) / (2 * a), "-", Sqrt(-delta)/(2 * a), "i")

def Get_num(str):
	i = 0
	num = ""
	is_float = False
	while (i < len(str)):
		if (str[i].isdigit() or (str[i] == '.' and is_float == False)):
			num += str[i]
			if (str[i] == '.'): is_float = True
			i += 1
		else:
			break
	return float(num), i + 1

def Get_power(str):
	l = len(str)
	if (l == 1):
		return 1
	elif (str[1] == '^'):
		signe = 1
		i = 2
		if (i >= l): Error("Expected a Number, found nothing.", 71)
		if str[2] == '-' or str[2] == '+':
			signe = 1 if str[2] == '+' else -1
			i = 3
		if (i >= l): Error("Expected a Number, found nothing.", 72)
		if (str[i].isdigit() == False): Error("Expected a Number, found '" + str[i] + "'.", 73)
		power, inc = Get_num(str[i:])
		if (inc + i - 1 != l): Error("Unexpected character '" + str[inc + i - 1]+ "'", 8)
		return power * signe

	else:
		Error("Expected '^' after X, found '" + str[1] + "'", 6)

def Term_eval(str, is_left):	#
	signe = 1 if is_left else -1
	signe *= 1 if str[0] == '+' else -1
	#print("-->", "-" if signe == -1 else "+", str[1:])
	power = 0
	coefficient = 0 # or 1 ?
	if (str[1].isdigit()):
		coefficient, inc = Get_num(str[1:]) # inc = number of bytes read + 1
		if (len(str) <= inc):
			power = 0
			return power, coefficient * signe
		elif (inc + 1 < len(str) and str[inc] == '*' and (str[inc + 1] == 'X' or str[inc + 1] == 'x')):

			power = Get_power(str[inc + 1:])
			return power,coefficient * signe
		else:
			Error("Unexpected character: '" + str[inc] + "'", 5)
	elif (str[1] == 'X' or str[1] == 'x'):
		coefficient = 1
		power = Get_power(str[1:])
		return power, coefficient * signe
	else:
		Error("Unexpected character after: '" + str[0] + "'", 4)


def Extract_pairs(str, is_left):
	#print("extracted pairs from:", str)
	i = 1
	s = str[0]
	while(i < len(str)):
		if(str[i] == '-' or str[i] == '+') and str[i - 1] != '^':
			power, coefficient = Term_eval(s, is_left)
			#print(power, coefficient)
			Add_pair(power, coefficient)
			s = str[i]
		else:
			s += str[i]
		i += 1
	power, coefficient = Term_eval(s, is_left)
	#print(power, coefficient)
	Add_pair(power, coefficient)

def Add_signe(s):
	for i in range(len(s)):
		if (s[i] == '+' or s[i] == '-') and (i + 1 >= len(s) or s[i + 1] == '+' or s[i + 1] == '-'):
			Error("Unexpected character after " + s[i])
	if (s[0] != '+' and s[0] != '-'):
		return "+" + s
	else:
		return s

def Parser(text):
	texts = text.replace(" ", "").split("=")
	if (len(texts) != 2):
		Error("Must have exactly one '='.\nEquation eg: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
	left = Add_signe(texts[0])
	right = Add_signe(texts[1])
	Extract_pairs(left, True)
	Extract_pairs(right, False)
	Validate_list()



if (len(sys.argv) != 2):
	Error("python3 computerv1.py [equation]\nEquation eg: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0", -1)
#print("equation: " + sys.argv[1] + "\n-------------------------")
#try:
Parser(sys.argv[1])
#except:
#	Error("Unknown Error. python3 computerv1.py [equation]", 1)
