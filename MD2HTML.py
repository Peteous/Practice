from Encode import htmlEncode

def urlParse(text):
	link = ''
	title = ''
	text = list(text)
	for char in text:
		if char == '[':
			start = text.index(char)
		if char == ']':
			mid1 = text.index(char)
		if char == '(':
			mid2 = text.index(char)
		if char == ')':
			end = text.index(char)
	for index in range(len(text)):
		if index > start and index < mid1:
			title += text[index]
		if index > mid2 and index < end:
			if text[index]=='&':
				link += '&amp;'
			else:
				link += text[index]
	if not link == '':
		return '<p>'+'<a href='+'\"'+link+'\">'+title+'</a></p>'
	else:
		print('No Markdown Links Found')
		return ''

def main():
	import clipboard
	string = clipboard.get()
	string = urlParse(string)
	print(string)
	
if __name__ == "__main__":
	main()