import os
import time
import pyqrcode
from PIL import Image

class QR_Gen(object):
    def __init__(self, text):
        self.qr_image = self.qr_generator(text)

    @staticmethod
    def qr_generator(text):
        qr_code = pyqrcode.create(text)
        timest=time.strftime("%d%m%y")
        file_name = f"QR-Code-{timest}"
        timest=time.strftime("%d%m%y")
        save_path = os.path.join(os.getcwd(), "output")
        name = f"{save_path}/{file_name}.png"
        qr_code.png(name, scale=10)
        image = Image.open(name)
        image = image.resize((400,400),Image.ANTIALIAS)
        image.show()

if __name__ == "__main__":
    QR_Gen(input("[QR] Enter text or link: "))
