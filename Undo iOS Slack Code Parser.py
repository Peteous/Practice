import clipboard

#Split code example for undoing:
#111111111 222222222 333333333 444444444 555555555 666666666 777777777 888888888 999999999 000000000

array = list(clipboard.get())
for index in range(90):
	if array[index] == ' ':
		array[index] = array[index+1]
		array.remove(array[index+1])

string = ''
for index in range(90):
	string += str(array[index])

clipboard.set(string)

#Output in clipboard:
#111111111222222222333333333444444444555555555666666666777777777888888888999999999000000000
