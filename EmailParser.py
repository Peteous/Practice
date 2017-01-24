import re

def emailExtract(String):
	pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
	match = re.search(pattern, String)
	try match:
		email = match.group()
		return email
	except:
		print("No Email Found - Null string passed")
		return ''
		
def checkEmailFormat(String):
	pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
	match = re.search(pattern, String)
	if match:
		return True
	else:
		return False