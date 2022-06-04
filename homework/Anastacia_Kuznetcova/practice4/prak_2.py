# Создайте текстовую переменную с текстом “fermentum”. Извлеките из строки первый
# символ, затем последний, третий с начала и третий с конца. Измерьте длину вашей
# строки.
ONE = "fermentum"
TWO = ONE[0]
print(TWO)
THREE = TWO[-1]
print(THREE)
FOUR = THREE[2]
print(FOUR)
FIVE = THREE[-3]
print(FIVE)
SIX = len(FIVE)
print(f"Длина строки = {SIX}")

