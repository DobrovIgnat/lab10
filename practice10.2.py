from PIL import Image

cards = {
    "1": "Новый год - new_year.jpg",
    "2": "8 Марта - march8.jpg",
    "3": "День рождения - birthday.jpg"
}

print("Выберите праздник:")
for num, text in cards.items():
    print(f"{num}. {text.split(' - ')[0]}")

choice = input("Введите цифру: ")

if choice in cards:
    try:
        filename = cards[choice].split(" - ")[1]
        Image.open(filename).show()
        print(f"Открытка '{filename}'")
    except:
        print("Ошибка: файл не найден")
else:
    print("Неправильный выбор")