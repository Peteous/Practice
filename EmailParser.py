import re

def emailExtract(String):
	pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
	match = re.search(pattern, String)
	if match:
		email = match.group()
		return email
	else:
		print("No Email Found - Null string passed")
		return ''
		
def checkEmailFormat(String):
	pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
	match = re.search(pattern, String)
	if match:
		return True
	else:
		return False