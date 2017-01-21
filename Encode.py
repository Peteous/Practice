def urlEncode(self,url,apiURL=None,paramDict=None):
	url = urlCharShift(url)
	if not apiURL == None:
		if not paramDict == None:
			dictKeys = urlCharShift(paramDict.keys())
			length = len(dictKeys)
			for index in range(length):	
				dictVars[index] = urlCharShift(paramDict[dictKeys[index]])
				output = '?'
			for i in range(length):
				if i < 1:
					output += dictKeys[i] + '=' + dictVars[i]
				else:
					output += '&' + dictKeys[i] + '=' + dictVars[i]
			return output
		else:
	else: 
def urlCharShift(self,text):
	url = str(text)
	url.replace('%','%25')
	url.replace('!','%21')
	url.replace('#','%23')
	url.replace('$','%24')
	url.replace('&','%26')
	url.replace('\'','%27')
	url.replace('(','%28')
	url.replace(')','%29')
	url.replace('*','%2A')
	url.replace('+','%2B')
	url.replace(',','%2C')
	url.replace('/','%2F')
	url.replace(':','%3A')
	url.replace(';','%3B')
	url.replace('=','%3D')
	url.replace('?','%3F')
	url.replace('@','%40')
	url.replace('[','%5B')
	url.replace(']','%5D')
	return url