#Library in Pythonista for iOS that handles actions for the clipboard (copy/paste) functionality
import clipboard

#Example Input:
#000000000111111111222222222333333333444444444555555555666666666777777777888888888999999999

array = list(clipboard.get())
codeLen = 9
for index in range(90):
	if index <= 8:
		if (index + 1)%codeLen == 0:
			array.insert(index+1,' ')
			index += 1
	elif (index+2)%10 == 0:
		array.insert(index+1,' ')
		index += 1

string = ''
for index in range(99):
	string += array[index]

clipboard.set(string)	

#Example Output:
#000000000 111111111 222222222 333333333 444444444 555555555 666666666 777777777 888888888 999999999
