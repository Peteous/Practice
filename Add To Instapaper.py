import appex
import requests
import clipboard

def urlEncode(address):
	address = str(address)
	address.replace('%','%25')
	address.replace('!','%21')
	address.replace('#','%23')
	address.replace('$','%24')
	address.replace('&','%26')
	address.replace('\'','%27')
	address.replace('(','%28')
	address.replace(')','%29')
	address.replace('*','%2A')
	address.replace('+','%2B')
	address.replace(',','%2C')
	address.replace('/','%2F')
	address.replace(':','%3A')
	address.replace(';','%3B')
	address.replace('=','%3D')
	address.replace('?','%3F')
	address.replace('@','%40')
	address.replace('[','%5B')
	address.replace(']','%5D')
	return address

def getInstapaperURL(webAddress):
	webAddress = str(webAddress)
	instapaper = 'https://www.instapaper.com/api/add'
	username = 'username@example.com'
	password = 'Example_Password_1'
	user = urlEncode(username)
	word = urlEncode(password)
	url = urlEncode(webAddress)
	instapaper += '?username='
	instapaper += user
	instapaper += '&password='
	instapaper += word
	instapaper += '&url='
	instapaper += url 
	return instapaper
	
def addToInstapaper(URL):
	clipboard.set(URL)
	
def main():
	if not appex.is_running_extension():
		print('Running in Pythonista app, using test data...\n')
		url = str(clipboard.get())
		if not url.startswith('http'):
			url = None
	else:
		url = appex.get_url()
	if url:
		print('Input URL: %s' % (url,))
		u = getInstapaperURL(url)
		print(u)
		addToInstapaper(u)
		print('\n\nComplete!')
	else:
		print('No input URL found.')

main()
