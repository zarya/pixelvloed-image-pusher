import sys
import argparse
from PIL import Image
from pixelvloed import PixelClient

parser = argparse.ArgumentParser()

parser.add_argument("--xoffset", "-x", help="X Offset", default=0, type=int)
parser.add_argument("--yoffset", "-y", help="Y Offset", default=0, type=int)
parser.add_argument("--file", "-f", help="File")
parser.add_argument("--server", "-s", help="Server")


args = parser.parse_args()
img = Image.open(args.file)
_, _, w, h = img.getbbox()
print(img.getbbox())

pixelflut = PixelClient(args.server, 5005, 0)

while True:
    for frame in range(0,img.n_frames):
        img.seek(frame)
        im = img.convert('RGB')
        for x in range(w):
            for y in range(h):
                r, g, b = im.getpixel((x, y))
                pixelflut.RGBPixel(x + args.xoffset,y + args.yoffset,r,g,b)
        pixelflut.flush()

