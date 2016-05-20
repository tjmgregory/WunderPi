from PIL import Image, ImageFont, ImageDraw

def draw(string):
	image = Image.new("RGBA", (1056,704), (255,255,255))
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype("courier-new.ttf", 100)
	draw.text((10, 0), string, (0,0,0), font=font)
	img_resized = image.resize((264,176), Image.ANTIALIAS)
	image.save('sample-out2.jpg')

draw("Cack")