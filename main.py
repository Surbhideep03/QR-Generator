try:
    import pyqrcode
    import png
    from pyqrcode import QRCode
    s = input("enter the text")
    url = pyqrcode.create(s)
    url.svg("myqr.svg", scale=8)
    url.png("myqr.png", scale=6)

    print("QR code generated successfully!")

except Exception as e:
    print("error")



