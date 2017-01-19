#These libraries are available in Pythonista for iOS
import appex
import requests
import clipboard

#This method is defined because urllib has very poor support in Pythonista for iOS.
#This method encodes the input string "address" with the character codes consistant with usability in a url
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

#This method creates a URL that when excecuted will add the input url, "webAddress", to Instapaper as a bookmark
def getInstapaperURL(webAddress):
	webAddress = str(webAddress)
	instapaper = 'https://www.instapaper.com/api/add'
	
	#The username and password should be altered by the user. They are set to example values for security reasons
	username = 'username@example.com'
	password = 'Example_Password_1'
	
	#This part of the method calls my urlEncode method to encode webAddress into instapaper, adding the proper requirements
	# for the API to function using URL encoding syntax
	user = urlEncode(username)
	word = urlEncode(password)
	url = urlEncode(webAddress)
	instapaper += '?username='
	instapaper += user
	instapaper += '&password='
	instapaper += word
	instapaper += '&url='
	instapaper += url 
	
	#return the encoded string for later use
	return instapaper

#This method executes the URL that adds desired url to Instapaper through url encoded input URL
def addToInstapaper(URL):
	#KNOWN ISSUE - see issues section
	# Pythonista for iOS doesn't support urllib well, so I resorted to setting the clipboard as the encoded url, which can
	# be pasted into your browser for bookmark adding
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
