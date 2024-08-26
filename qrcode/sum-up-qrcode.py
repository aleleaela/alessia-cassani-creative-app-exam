import segno

qrcode = segno.make_qr("https://github.com/aleleaela/alessia-cassani-creative-app-exam")
qrcode.to_pil()

(qrcode.to_pil(scale=9,dark="lightcoral", light="lightblue", border=1)
.save("image/qrcode.png"))

