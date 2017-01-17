#Library in Pythonista for iOS that handles actions for the clipboard (copy/paste) functionality
import clipboard

#Example Input:
#000000000111111111222222222333333333444444444555555555666666666777777777888888888999999999

#Establish an array of 90 characters from the clipboard
array = list(clipboard.get())

#Define the length of each recovery code as 9 characters, which is what Slack uses
codeLen = 9

#Iterate through the 90 copied characters from thr clipboard array, inserting spaces after every 9 characters are parsec
for index in range(90):
	if index <= 8:
		if (index + 1)%codeLen == 0:
			array.insert(index+1,' ')
			index += 1
	elif (index+2)%10 == 0:
		array.insert(index+1,' ')
		index += 1

#Establish a blank string which can be added to based upon the adjusted array made in previous step
string = ''

#Add the characters from the array to the string, covering all 99 characters
for index in range(99):
	string += array[index]

#Save the string to the clipboard
clipboard.set(string)	

#Example Output:
#000000000 111111111 222222222 333333333 444444444 555555555 666666666 777777777 888888888 999999999
