from PIL import Image, ImageDraw, ImageFont

image_path = "foto.png"
font_path = "reddit.ttf"

font = ImageFont.truetype(font_path, 36)

positions = [(280, 335), (280, 725), (280, 1115), (280, 1505), (280, 1893), (980, 335), (980, 725), (980, 1115), (980, 1505), (980, 1893)]

start_number = 1

for i in range(1, 11):
    image = Image.open(image_path)  # Abre uma nova imagem em cada iteração
    draw = ImageDraw.Draw(image)
    
    numbers = [start_number + (n % 5) for n in range(10)]  # Calcula os números a serem desenhados
    
    for pos, num in zip(positions, numbers):
        draw.text(pos, str(num), fill="black", font=font)

    image.save(f"rifa{i}.png")
    start_number += 5  # Incrementa o número inicial para a próxima iteração
