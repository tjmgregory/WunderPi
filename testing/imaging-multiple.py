from PIL import Image, ImageFont, ImageDraw
import json
import textwrap

indent = 20
textSize = 18
spacing = 6
font = ImageFont.truetype("courier-new.ttf", textSize)
fontpixels = font.getsize('a')

# 9 lines possible at size 18

def draw(content, fileName="test"):
	image = Image.new("RGBA", (264,176), (255,255,255))
	draw = ImageDraw.Draw(image)

	prelined_tasks = split(content)

	pixelHeight = 0
	for prelined_task in prelined_tasks:
		for line in prelined_task:
			draw.text((indent, pixelHeight), line, (0,0,0), font=font)
			pixelHeight += textSize
		pixelHeight += spacing

	image.save(fileName+'.jpg')


# Returns an array of arrays which hold split up tasks
def split(content):
	holder = []

	for task in content:
		charsToWrapBy = textSize*4.0/3.0-((indent+fontpixels[0])/fontpixels[0])
		wrapped = textwrap.wrap(task, charsToWrapBy)
		holder.append(wrapped)

	return holder