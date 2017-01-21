class Encode:
	def __init__(self):
		output = ''
	class url(Encode):
		def urlEncode(self,URL):
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
		def urlWrite(self,URL,encodedStr):
			output = URL + '?' + encodedStr
			return output