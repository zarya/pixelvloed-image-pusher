import numpy as np
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
frameArray = [] 
for frame in range(0,img.n_frames):
    img.seek(frame)
    im = img.convert('RGB').rotate(90)
    frameArray.append(np.array(im))

while True:
    for frame in frameArray:
        for y in range(w):
            for x in range(h):
                r, g, b = frame[x,y] 
                pixelflut.RGBPixel(x + args.xoffset,y + args.yoffset,r,g,b)
        pixelflut.flush()
