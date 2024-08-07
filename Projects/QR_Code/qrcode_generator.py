# Create QR Code
import qrcode
data = 'morfiq QR code'
img = qrcode.make(data)
img = qr.make_image(fill_color="red", back_color="white")
img.save(r'C:\path\to\qrcode\image\myqrcode.jpg')




