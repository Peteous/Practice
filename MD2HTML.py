def urlParse(text):
	_link = ''
	_title = ''
	text = list(text)
	for char in text:
		if char == '[':
			__start = text.index(char)
		if char == ']':
			mid1 = text.index(char)
		if char == '(':
			mid2 = text.index(char)
		if char == ')':
			__end = text.index(char)
	for index in range(len(text)):
		if index > __start and index < mid1:
			_title += text[index]
		if index > mid2 and index < __end:
			if text[index]=='&':
				_link += '&amp;'
			else:
				_link += text[index]
	if not _link == '':
		return '<p>'+'<a href='+'\"'+_link+'\">'+_title+'</a></p>'
	else:
		print('No Markdown Links Found')
		return ''

#Does not handle literal asterisks \*
def italicsParse(text):
	text = list(text)
	output = ''
	__first = 0
	for char in text:
		if char == '*' and __first == 0:
			if not text[text.index(char)+1] == '*':
				__start = text.index(char)
				__first == 1
			#Escape case for finding bold-marked text
			else:
				__first = 2
		if char == '*' and __first == 1:
			if not text[text.index(char)+1] == '*':
				__end = text.index(char)
				__first == 2
			else:
				__first = 2
	if __start == None or __end == None:
		print('No italics found')
		return ''
	else:
		for index in range(len(text)):
			if index > __start and index < __end:
				output += text[index]
		if not output == '':
			return '<em>'+output+'</em>'
		else:
			print('No italics found')
			return ''

#does not handle literal underscores \_
def underParse(text):
	text = list(text)
	output = ''
	__first = 0
	for char in text:
		if char == '_' and __first == 0:
			if not text[text.index(char)+1] == '_':
				__start = text.index(char)
				__first == 1
			#Escape case for finding bold-marked text
			else:
				__first = 2
		if char == '_' and __first == 1:
			if not text[text.index(char)+1] == '_':
				__end = text.index(char)
				__first == 2
			else:
				__first = 2
	if __start == None or __end == None:
		print('No underscores found')
		return ''
	else:
		for index in range(len(text)):
			if index > __start and index < __end:
				output += text[index]
		if not output == '':
			return '<em>'+output+'</em>'
		else:
			print('No underscores found')
			return ''

def boldParse(text):
	text = list(text)
	output = ''
	__first = 0
	for char in text:
		if char == '_' and __first == 0:
			if text[text.index(char)+1] == '_':
				__start = text.index(char)
				__first == 1
			#Escape case for finding italic-marked text
			else:
				__first = 2
		if char == '_' and __first == 1:
			if text[text.index(char)+1] == '_':
				__end = text.index(char)
				__first == 2
			else:
				__first = 2
	if __start == None or __end == None:
		print('No double asterisks found')
		return ''
	else:
		for index in range(len(text)):
			if index > __start+1 and index < __end:
				output += text[index]
		if not output == '':
			return '<strong>'+output+'</strong>'
		else:
			print('No double asterisks found')
			return ''

def _parse(text,char,num,tag):
	text = list(text)
	output = ''
	__endtag = '</'+tag.strip('<>')+'>'
	__first = 0
	for letter in text:
		if num == 1:
			if letter == char and __first == 0:
				if not text[text.index(letter)+1] == char:
					__start = text.index(letter)
					__first == 1
				#Escape case for finding repeat char
				else:
					__first = 2
			if letter == char and __first == 1:
				if not text[text.index(letter)+1] == char:
					__end = text.index(char)
					__first == 2
				else:
					__first = 2
		if num = 2:
			if letter == char and __first == 0:
				if text[text.index(letter)+1] == char:
					__start = text.index(letter)
					__first == 1
				#Escape case for not finding repeat char
				else:
					__first = 2
			if letter == char and __first == 1:
				if text[text.index(letter)+1] == char:
					__end = text.index(char)
					__first == 2
				else:
					__first = 2
		else:
			print('Input number not recognized')
			return ''
		
	if __start == None or __end == None:
		print('No \"' + char + '\" tags were found')
		return ''
	else:
		for index in range(len(text)):
			if num == 2:
				if index > __start+1 and index < __end:
					output += text[index]
			if num == 1:
				if index > __start and index < __end:
					output += text[index]
		if not output == '':
			return tag+output+__endtag
		else:
			print('No output could be generated')
			return ''

#Only runs through string once
def main():
	import clipboard
	string = clipboard.get()
	if string == None:
		string = input("Type or paste your Markdown formatted text here:\n")
	string = urlParse(string)
	print(string)

if __name__ == "__main__":
	main()
