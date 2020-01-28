from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from pathlib import Path

path = Path(__file__).parent / "../assets/sample.jpg"

img = Image.open(path)
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("sans-serif.ttf", 16)
draw.text((0, 0),"Sample Text",(255,255,255))
img.save('sample-out.jpg')