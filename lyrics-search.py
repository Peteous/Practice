try:
	import appex
	importSuccess = True
except ImportError as e:
	print(e.with_traceback)
	print('This is a Pythonista library')
	importSuccess = False
import webbrowser
from Encode import urlEncode

def main():
	if importSuccess == True:
		if not appex.is_running_extension():
			query = str(input('What song name or lyrics excerpt are you looking for?\n'))
		else:
			query = str(appex.get_text())
	else:
		query = str(input('What song name or lyrics excerpt are you looking for?\n'))
	apiURL = 'https://duckduckgo.com/'
	paramNames = ['q','t','ia']
	paramData = [query.replace(' ','+'),'ipad','lyrics']
	print(paramData)
	query = urlEncode(None,apiURL,paramNames,paramData)
	print(query)
	webbrowser.open(query)

if __name__ == '__main__':
	main()