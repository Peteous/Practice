
#These libraries are available in Pythonista for iOS
import appex
import requests
import clipboard

#import urlEncode method from my Encode file
from Encode import urlEncode

#This method creates a URL that when excecuted will add the input url, "webAddress", to Instapaper as a bookmark
def getInstapaperURL(webAddress):
	webAddress = str(webAddress)
	instapaper = 'https://www.instapaper.com/api/add'
	
	#The username and password should be altered by the user. They are set to example values for security reasons
	paramNames = ['username','password']
	paramData = ['username@example.com','Example_Password_1']
	
	#This part of the method calls urlEncode method from Encode.py to encode webAddress w/ parameters & return
	return urlEncode(webAddress,instapaper,paramNames,paramData)

#This method executes the URL that adds desired url to Instapaper through url encoded input URL
def addToInstapaper(URL):
	#clear the clipboard, since that's no longer necessary
	clipboard.set('')
	
	#Library that pythonista can use to open urls
	import webbrowser
	
	#executes url by opening url in web browser
	webbrowser.open(URL)
	
#Main method
def main():
	#Check to see if the main method is being run from the share sheet
	if not appex.is_running_extension():
		#if this if statement is true, clarify that we're running in the app
		print('Running in Pythonista app, using test data...\n')
		
		#get the clipboard for the url
		url = str(clipboard.get())
		
		#check that the clipboard is a url. if not, set as None for error production
		if not url.startswith('http'):
			url = None
	else:
		#Get url from app extension if running from extension
		url = appex.get_url()
	
	#Check if url has a value
	if url:
		#Give user feedback about what is happening
		print('Input URL: %s' % (url,))
		
		#Get the instapaper URL for adding url as bookmark
		u = getInstapaperURL(url)
		
		#Add u to Instapaper 
		addToInstapaper(u)
		
		#Tell  the user that the action is complete
		print('\n\nComplete!')
	else:
		#Tell the user that there was an error
		print('No input URL found.')

#Execute main function if this is the main script
if __name__ == '__main__':
	main()