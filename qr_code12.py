import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   
                   box_size=10,border=4,)

qr.add_data("https://www.linkedin.com/in/muhammad-fida-hussain/")

qr.make(fit=True)

img=qr.make_image(fill_color="darkgreen",back_color="black")
img.save("FidaHussain_.png")
print("Qr is Ready")