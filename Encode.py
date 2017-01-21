def urlEncode(url,apiURL=None,paramNames=None,paramData=None):
	output = ''
	url = urlCharShift(url)
	url = 'url='+url
	if not paramNames == None and not paramData == None and not apiURL == None:
		output += apiURL
		output += '?'
		length = len(paramNames)
		for index in range(length):
			paramData[index] = urlCharShift(paramData[index])
			if index < 1:
				output += paramNames[index] + '=' + paramData[index]
			else:
				output += '&' + paramNames[index] + '=' + paramData[index]
		output += '&'
		output += url
		return output
	elif paramNames == None and not apiURL == None:
		output += apiURL
		output += '?'
		output += url
		return output
	elif apiURL == None:
		length = len(paramNames)
		for index in range(length):
			paramData[index] = urlCharShift(paramData[index])
			if index < 1:
				output += paramNames[index] + '=' + paramData[index]
			else:
				output += '&' + paramNames[index] + '=' + paramData[index]
		output += url
		return output
	else:
		print('\n\nAn error occured. Please check your input parameters.')
		return output

#internal method
def urlCharShift(text):
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