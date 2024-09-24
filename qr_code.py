# Simple QR Code

# import qrcode as qr
# img = qr.make("https://www.instagram.com/maaahiiii_1111/")
# img.save("Mehul_instagram_qr.png")

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4)

qr.add_data("https://www.facebook.com/mehul.agarwal.52438")
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="blue")   
img.save("mehul_fb.png")                
