# Square ~300px headshots from Wikimedia Commons originals (see assets/players/credits.json)
from PIL import Image, ImageOps
import os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'assets','players')
# (centre_x, centre_y, side) as fractions of image width
CROPS={'kohli':(0.44,0.52,0.80),'gill':(0.48,0.38,0.62),'rohit':(0.52,0.36,0.58)}
for k,(cx,cy,s) in CROPS.items():
    im=ImageOps.exif_transpose(Image.open(f'{D}/original/{k}.jpg')).convert('RGB'); w,h=im.size
    side=int(s*w); x=int(cx*w-side/2); y=int(cy*h-side/2)
    x=max(0,min(x,w-side)); y=max(0,min(y,h-side))
    im.crop((x,y,x+side,y+side)).resize((300,300),Image.LANCZOS).save(f'{D}/{k}.jpg',quality=88)
    print(k,w,h,'->',(x,y,side))
