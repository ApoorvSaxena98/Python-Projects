#import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
#a = "https://www.google.co.in"

# Generate QR code
#url = pyqrcode.create(a)

# Create and save the png file naming "pyqr.png"
#url.svg("pyqr.svg", scale=6)


import pyqrcode
img = pyqrcode.create('https://www.google.co.in')
img.svg('F:\PythonProjects\PP\pqr.svg', scale=4)