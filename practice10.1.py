from PIL import Image

img = Image.open('123.jpg')

width, height = img.size
new_height = height - 150

area = (0, 0, width, new_height)

cropped_img = img.crop(area)
cropped_img.save('cropped_image.jpg')

print(f"Новый размер: {width}x{new_height}")