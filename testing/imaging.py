from PIL import Image, ImageFont, ImageDraw

def draw(content, fileName):
	image = Image.new("RGBA", (1056,704), (255,255,255))
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype("courier-new.ttf", 100)
	draw.text((10, 0), content, (0,0,0), font=font)
	# img_resized = image.resize((264,176), Image.ANTIALIAS)
	image.save(fileName+'.jpg')
