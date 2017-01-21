def encode(self,URL):
	output = str(URL)
	output.replace('%','%25')
	output.replace('!','%21')
	output.replace('#','%23')
	output.replace('$','%24')
	output.replace('&','%26')
	output.replace('\'','%27')
	output.replace('(','%28')
	output.replace(')','%29')
	output.replace('*','%2A')
	output.replace('+','%2B')
	output.replace(',','%2C')
	output.replace('/','%2F')
	output.replace(':','%3A')
	output.replace(';','%3B')
	output.replace('=','%3D')
	output.replace('?','%3F')
	output.replace('@','%40')
	output.replace('[','%5B')
	output.replace(']','%5D')
	return output
def params(self,paramDict):
	dictKeys = paramDict.keys()
	length = len(dictKeys)
	for index in range(length):
		dictVars[index] = paramDict[dictKeys[index]]
	output = '?'
	for i in range(length):
		if i < 1:
			output += dictKeys[i] + '=' + dictVars[i]
		else:
			output += '&' + dictKeys[i] + '=' + dictVars[i]
	return output
def write(self,URL,encodedStr):
	output = URL + '?' + encodedStr
	return output