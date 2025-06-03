try:
    num1 = int(input("Введите число: "))
    result = num1 / 0
    print("Результат:", result)
except ZeroDivisionError:
    print("Нельзя делить на ноль!")


try:
    num = int(input("Введите целое число: "))
    print("Вы ввели:", num)
except ValueError:
    print("Ошибка: нужно ввести только целое число!")


try:
    file = open("myfile.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Ошибка: файл не найден.")

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    
    # Попробуем сложить как числа
    result = int(a) + int(b)
    print("Сумма:", result)
except ValueError:
    print("Ошибка: ввод должен быть числом.")
except TypeError:
    print("Ошибка: типы данных не совпадают.")


try:
    with open("readonly.txt", "w") as file:
        file.write("Пробуем записать текст.")
except PermissionError:
    print("Ошибка: нет разрешения на запись в файл.")

try:
    my_list = [10, 20, 30]
    index = int(input("Введите индекс: "))
    print("Значение по индексу:", my_list[index])
except IndexError:
    print("Ошибка: индекс вне диапазона списка.")


try:
    num = int(input("Введите число (или нажмите Ctrl+C для отмены): "))
    print("Вы ввели:", num)
except KeyboardInterrupt:
    print("\nВы прервали ввод (KeyboardInterrupt).")


try:
    a = int(input("Введите числитель: "))
    b = int(input("Введите знаменатель: "))
    result = a / b
    print("Результат деления:", result)
except ArithmeticError:
    print("Произошла арифметическая ошибка.")

try:
    with open("file.txt", "r", encoding="utf-8") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Ошибка кодировки при чтении файла.")
except FileNotFoundError:
    print("Файл не найдено")


try:
    my_list = [1, 2, 3]
    my_list.upper()  # специально неправильную операцию сделала
except AttributeError:
    print("Ошибка: у списка нет такого метода.")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


n = int(input("Сколько строк прочитать? "))
with open("example.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        if line == "":
            break  # файл закончился
        print(line.strip())



text = input("Введите текст для добавления в файл: ")

# Добавляем текст
with open("example.txt", "a") as file:
    file.write(text + "\n")

# Читаем и выводим всё содержимое файла
with open("example.txt", "r") as file:
    print("\nСодержимое файла:")
    print(file.read())


n = int(input("Сколько последних строк прочитать? "))
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line.strip())

with open("example.txt", "r") as file:
    lines = file.readlines()

print("Список строк:", lines)

file = open("example.txt", "r")
print("Файл закрыт?", file.closed)  
file.close()
print("Файл закрыт?", file.closed)  


with open("example.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

print("Строки без переносов:", lines)


with open("example.txt", "r") as file:
    text = file.read()

# Удалим запятые и точки, чтобы не мешали
cleaned_text = text.replace(",", " ").replace(".", " ")
words = cleaned_text.split()
print("Количество слов:", len(words))


filenames = ["file1.txt", "file2.txt"]
chars = []

for name in filenames:
    try:
        with open(name, "r") as f:
            content = f.read()
            chars.extend(list(content))  # добавляем все символы
    except FileNotFoundError:
        print(f"Файл {name} не найден.")

print("Список символов:", chars)



import string

for letter in string.ascii_uppercase:  # A до Z
    filename = f"{letter}.txt"
    with open(filename, "w") as file:
        file.write(f"Это файл {letter}\n")



import string

n = int(input("Сколько букв на каждой строке? "))
alphabet = string.ascii_lowercase

with open("alphabet.txt", "w") as file:
    for i in range(0, len(alphabet), n):
        line = alphabet[i:i+n]
        file.write(line + "\n")

















































