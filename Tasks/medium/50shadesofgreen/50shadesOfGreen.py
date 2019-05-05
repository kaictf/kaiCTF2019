# -*- coding: utf-8 -*
# Создание изображения:
from PIL import Image, ImageDraw

flag = "kaiCTF{s0m3_f1@g1234}"
#print([ord(i) for i in flag])

color = (0, 0, 0)

img = Image.new('RGB', (len(flag)*50, 50), color) # создаем картинку в высоту 50 и в ширину равной длине флага * 50

draw = ImageDraw.Draw(img)

for i in range(len(flag)):
	draw.rectangle((((i)*50,0), ((i+1)*50, 50)), fill=(0, ord(flag[i]), 0)) # рисуем квадратики 50 на 50, где hex-код символа - оттенок зеленого цвета


img.save("task-example.png")

#Вариант решения таска

img = Image.open("task-example.png") #открываем картинку
size = w, h = img.size 				#берем ее размеры
data = img.load()					#загружаем в память

pixels = [data[x,0][1] for x in range(w)] #читаем оттенок зеленого цвета из ОДНОЙ строчки пикселей
flagDec = chr(pixels[0]) # сохраняем первый пиксель как первый символ
for i in pixels: #бегаем по пикселям и сохраняем новые символы
	if (flagDec[-1] != chr(i)):
		flagDec += chr(i)


print(flagDec)






"""draw = ImageDraw.Draw(source_img)
draw.rectangle(((0, 00), (100, 100)), fill="black")

source_img.save(out_file, "JPEG")


from PIL import Image, ImageDraw
color = (0, 0, 120)
img = Image.new('RGB', (100, 50), color)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((10, 20), text)
img.save("pil-basic-example.png")
"""