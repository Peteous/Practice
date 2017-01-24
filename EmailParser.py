import re

#Method for parsing input String for an email address formatted substring
def emailExtract(String):
	pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
	match = re.search(pattern, String)
	if match:
		email = match.group()
		return email
	else:
		print("No Email Found - Null string passed")
		return ''
		
#Method for checking validity of input email based on format
def checkEmailFormat(String):
	pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
	match = re.search(pattern, String)
	if match:
		return True
	else:
		return False