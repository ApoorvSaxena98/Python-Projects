import pyqrcode
img = pyqrcode.create('https://www.google.co.in')
img.svg('F:\PythonProjects\PP\pqr.svg', scale=4)