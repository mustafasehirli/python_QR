

import pyqrcode

url = input("url giriniz : ")

qr_cod = pyqrcode.create(url)
qr_cod.svg("qrcode.svg",scale=5)