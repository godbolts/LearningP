import random
import webbrowser
x_lagi = 85.0
x_põhi = -85.0
y_lagi = 180.0
y_põhi = -180.0
pikk = 6
x_toor = random.uniform(x_lagi, x_põhi)
y_toor = random.uniform(y_lagi, y_põhi)
x = str(format(x_toor, f'.{pikk}f'))
y = str(format(y_toor, f'.{pikk}f'))
url = f'https://maps.google.com/?q={x},{y}'
webbrowser.open(url)