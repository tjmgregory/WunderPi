from PIL import Image, ImageFont, ImageDraw

def draw(content, fileName="test"):
	image = Image.new("RGBA", (264,176), (255,255,255))
	draw = ImageDraw.Draw(image)

	textSize = 18
	font = ImageFont.truetype("courier-new.ttf", textSize)
	y = 0
	for task in content:
		draw.text((10, y), task, (0,0,0), font=font)
		y = y + textSize

	image.save(fileName+'.jpg')
