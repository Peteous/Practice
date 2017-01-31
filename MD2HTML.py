import re
from Encode import htmlEncode

_text = r"[\S]*"
_link = r"http[s]?://"
_linkBrackets = "\[.+?\]\(^https?:\/\/.+?\)"

def urlParse(text):
	mdLink = re.findall(_linkBrackets,text)
	print(mdLink)
	if not mdLink == None:
		ahref = str(re.findall(r"("+_link+r")",str(mdLink)))
		ahref = ahref.strip('()')
		ahref = htmlEncode(ahref)
		ahref = '<a href='+'\"'+ahref+'\">'
		p = str(re.findall(r"["+_text+r"]",str(mdLink)))
		p.strip('()')
		p = p+r"</a>"
		p = ahref + p
		return '<p>' + p + '</p>'
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