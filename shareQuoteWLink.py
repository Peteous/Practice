import appex, ui
import os
from math import ceil, floor
import requests
import clipboard
import webbrowser

#import Launcher.py
	#This script is available in pythonista, but could not be imported for some reason
'''
This widget script shows a grid of shortcut buttons that launch URLs when tapped.

The shortcut titles/URLs and the grid layout can be configured with the SHORTCUTS, COLS, ROWS variables.
'''

# NOTE: The ROWS variable determines the number of rows in "compact" mode. In expanded mode, the widget shows all shortcuts.
COLS = 3
ROWS = 2

# Option included are for the three writing apps I've used recently - Notes.app, Bear, and iA Writer
# Each shortcut should be a dict with at least a 'title' and 'url' key. 'color' and 'icon' are optional. If set, 'icon' should be the name of a built-in image.
SHORTCUTS = [
{'title': 'Notes', 'url': 'notes://', 'color': '#c7d200', 'icon': 'iow:clipboard_24'},
{'title': 'iA Writer', 'url': 'iawriter://', 'color': '#000000', 'icon': 'iow:compose_24'},
{'title': 'Bear', 'url': 'bear://', 'color': '#ff0000', 'icon': 'iow:document_text_24'},
]

class LauncherView (ui.View):
	def __init__(self, shortcuts, *args, **kwargs):
		row_height = 110 / ROWS
		super().__init__(self, frame=(0, 0, 300, ceil(len(shortcuts) / COLS) * row_height), *args, **kwargs)
		self.buttons = []
		for s in shortcuts:
			btn = ui.Button(title=' ' + s['title'], image=ui.Image(s.get('icon', 'iow:compass_24')), name=s['url'], action=self.button_action, bg_color=s.get('color', '#55bcff'), tint_color='#fff', corner_radius=9)
			self.add_subview(btn)
			self.buttons.append(btn)
	
	def layout(self):
		bw = self.width / COLS
		bh = floor(self.height / ROWS) if self.height <= 130 else floor(110 / ROWS)
		for i, btn in enumerate(self.buttons):
			btn.frame = ui.Rect(i%COLS * bw, i//COLS * bh, bw, bh).inset(2, 2)
			btn.alpha = 1 if btn.frame.max_y < self.height else 0
	
	def button_action(self, sender):
		webbrowser.open(sender.name)
#End import Launcher.py

def main():
	url = ''
	quote = clipboard.get()
	quote = quote.capitalize()
	if not appex.is_running_extension():
		print('Error: Running in Pythonista App. Cannot get URL\n')
	else:
		url = appex.get_url()
		webbrowser.open('pythonista3://')
	if not url == '':
		print('Error: No input URL found.')
	clipboard.set('['+quote+']('+url+')')
	widget_name = __file__ + str(os.stat(__file__).st_mtime)
	v = appex.get_widget_view()
	# Optimization: Don't create a new view if the widget already shows the launcher.
	if v is None or v.name != widget_name:
		v = LauncherView(SHORTCUTS)
		v.name = widget_name
		appex.set_widget_view(v)
		
if __name__ == '__main__':
	main()