import appex
import webbrowser
from Encode import urlEncode

def main():
	if not appex.is_running_extension():
		query = str(input('What song name or lyrics excerpt are you looking for?\n'))
	else:
		query = str(appex.get_text())
	apiURL = 'https://duckduckgo.com/'
	paramNames = ['q','t','ia']
	paramData = [query.replace(' ','+'),'ipad','lyrics']
	print(paramData)
	query = urlEncode(None,apiURL,paramNames,paramData)
	print(query)
	webbrowser.open(query)

if __name__ == '__main__':
	main()