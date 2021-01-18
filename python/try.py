# Python3 program to Convert a
# list to dictionary

def Convert(lst):
	res_dct = {enumerate(lst): lst}
	return res_dct

# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))
