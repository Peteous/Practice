import re

_text = r"[\S]*"
_linkBrackets = r"\["+_text+r"\]\("+_text+r"\)"

def urlParse(text):
    
