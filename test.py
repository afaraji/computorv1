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

pairs = [(0, 0), (1, 0), (2, 0)]

def Error(text, error_num):
	print("\x1b[6;30;41mERROR:\x1b[0m", text)
	exit(error_num)

def Parser(text):
	lol = text.replace(" ", "")
	print(lol)
	Error("wrong dadadada lol p.", 2)

tt = "-    5     * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Parser(tt)
