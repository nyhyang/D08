# Borrowed from https://realpython.com/learn/python-first-steps/

###############################################################################
# Modify the variables so that all of the statements evaluate to True. ########
###############################################################################

var1 = 1
var2 = 'psdfgn'
var3 = [1, 2, 3, 4, 5]
var4 = (1, 2, "Hello, Python!")
var5 = {"happy" : 7, "egg" : "salad", "tuna" : "fish"}
var6 = 2.0

d = {1:'blue', 2: 'green', 3:'green'}
def reverse_lookup(dict_, value):
	# method 1
	key_or_keys = []
	for key in dict_:
		if dict_[key] == value:
			key_or_keys.append(key)
	return key_or_keys

		# if values == value:
		# 	return key
		# else:
		# 	return ValueError
	# method 2
	# ket_or_keys = []
	# for key in dict_:
	# 	if dict_[key] == value:
	# 		ket_or_keys.append(key)
	# return ket_or_keys

	# method 3
	# for key, val in dic_.item():
	# 	if val == value:
	# 		key_or_keys.append(key)
	# return key_or_keys


###############################################################################
# Don't edit anything below this comment ######################################
###############################################################################

print(reverse_lookup(d, 'green'))


# integers
print(type(var1) is int)
print(type(var6) is float)
print(var1 < 35)
print(var1 <= var6)

# strings
print(type(var2) is str)
print(var2[5] == 'n' and var2[0] == "p")

# lists
print(type(var3) is list)
print(len(var3) == 5)

# tuples
print(type(var4) is tuple)
print(var4[2] == "Hello, Python!")

# dictionaries
print(type(var5) is dict)
print("happy" in var5)
print(7 in var5.values())
print(var5.get("egg") == "salad")
print(len(var5) == 3)
var5["tuna"] = "fish"
print(len(var5) == 3)