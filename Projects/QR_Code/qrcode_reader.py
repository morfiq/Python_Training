# Read QR Code
from pyzbar.pyzbar import decode
from PIL import Image
img = Image.open(r"C:\path\to\qrcode\image\myqrcode.jpg")
result = decode(img)
print(result)