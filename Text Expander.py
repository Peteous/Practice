def readFile(str(filename)):
	entries = []
	with open(filename,'r') as file:
		for line in file:
			entries.append(file.readline())
	file.close()
	return entries
	
def getShortcuts():
	fileEntries = readFile('shortcuts.txt')
	string = ''
	xcuts = []
	end = False
	for index in range(len(fileEntries)):
		for char in fileEntries[index]:
			if not char == '=' and end == False:
				string += char
			elif char == '=':
				end = True
		xcuts[index] = string
	return xcuts
	
def getExpansions():
	fileEntries = readFile('shortcuts.txt')
	string = ''
	expansions = []
	end = False
	for index in range(len(fileEntries)):
		for char in fileEntries[index]:
			if not char == '=' and end == True:
				string += char
			elif char == '=':
				end = True
		expansions.append(string)
	return expansions
	
def main():
	shorts = getShortcuts()
	longs = getExpansions()
	filename = input('What is the name of your text file?')
	text = []
	with open(filename,'r') as file:
		for line in file:
			text.append(file.readline())
	file.close()
	for line in text:
		for entry in shorts:
			if line.contains(entry):
				i = entry.index
				line.replace(entry,longs[i])
	with open('output.txt','w') as output:
		for line in text:
			output.write(line)
	file.close()
	
if __name__ == '__main__':
	main()