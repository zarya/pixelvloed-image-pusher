import sys
from PIL import Image
from pixelvloed import PixelClient

host = "100.65.0.2"
#host = "127.0.0.1"

img = Image.open(sys.argv[1])
_, _, w, h = img.getbbox()
print(img.getbbox())
bands = img.getbands()
if "A" in bands:
    mode = 1 
else:
    mode = 0 

pixelflut = PixelClient(host, 5005, mode)

while True:
    for x in range(w):
        for y in range(h):
            if mode == 1:
                r, g, b, a = img.getpixel((x, y))
                pixelflut.RGBPixel(x,y,r,g,b,a)
            else:
                r, g, b = img.getpixel((x, y))
                pixelflut.RGBPixel(x,y,r,g,b)
    pixelflut.flush()
    img = Image.open(sys.argv[1])

