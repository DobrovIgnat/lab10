from PIL import Image, ImageDraw, ImageFont

img = Image.open("cropped_image.jpg")
draw = ImageDraw.Draw(img)

name = input("Кого поздравляем? ")

try:
    font = ImageFont.truetype("arialbd.ttf", 40)  # Arial Bold
except:
    try:
        font = ImageFont.truetype("Roboto-Bold.ttf", 40)  # Roboto Bold
    except:
        font = ImageFont.load_default(size=40)

text = f"{name}, поздравляю!"
text_width = draw.textlength(text, font=font)  # Теперь draw определен

x = (img.width - text_width) / 2
y = img.height - 100

draw.text((x, y), text, font=font, fill="red")

img.save("otkrytka_s_podpis.png")
print("Открытка сохранена как 'otkrytka_s_podpis.png'")
img.show()