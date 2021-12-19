# pairs = [(0, 0), (1, 0), (2, 0)] # pars: (power, coefficient)

# def is_power_in_list(power):
# 	for i in range(len(pairs)):
# 		if pairs[i][0] == power:
# 			return i
# 	return -1

# def sort_by_power(e):
# 	return e[0]

# def Add_pair(power, coefficient):
# 	position = is_power_in_list(power)
# 	if (position < 0):
# 		pairs.insert(position, (power,coefficient))
# 		pairs.sort(key=sort_by_power)
# 	else:
# 		pairs[position] = (power,coefficient + pairs[position][1])

# print(pairs)
# Add_pair(7, 3)
# print(pairs)
# Add_pair(5, 3)
# print(pairs)
# for x in pairs[:]:
# 	if(x[0] > 2):
# 		pairs.remove(x)
# print(pairs)
#--------------------------------------
# SQUARE = "\u00B2"
# pairs = [(0, 0), (1, 0), (2, 0)]

# def Error(text, error_num):
# 	print("\x1b[6;30;41mERROR:\x1b[0m", text)
# 	exit(error_num)

# def Parser(text):
# 	lol = text.replace(" ", "")
# 	print("testing:" + SQUARE,lol)
# 	Error("wrong dadadada lol p.", 2)

# tt = "-    5     * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# Parser(tt)
#------------------------------------------
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

	return float(num), i + 1 # or i + 1 ?

str = "-55.12*X"
coefficient, inc = Get_num(str[1:])
print(coefficient, "|", str[inc])


"5 * x^*32 = 0"
"5 *x^2 = 100 *"

