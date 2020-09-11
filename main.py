import qrcode
from PIL import Image,ImageDraw
import os
data = input("Enter your data or link : ")
img = qrcode.make(data)
img.save("1.png")
os.startfile("1.png")
print("Thank You ... Your ID has been generated")
        
