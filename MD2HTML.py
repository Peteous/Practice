import re
from Encode.py import htmlEncode

_text = r"[\S]*"
_link = r"http[s]?://"
_linkBrackets = r"["+_text+r"]("+_link+r")"

def urlParse(text):
    mdLink = re.findall(_linkBrackets)
    if mdLink:
        ahref = str(re.findall(r"("+_link+r")",mdLink))
        ahref.strip(['(',')'])
        ahref = htmlEncode(ahref)
        ahref = '<a href='+'\"'+ahref+'\">'
        p = re.findall(r"["+_text+r"]",mdLink)
        p.strip(['[',']'])
        p = p+r"</a>"
        p = ahref + p
        return '<p>' + p + '</p>'
    else:
        print('No Markdown Links Found')
        return ''
