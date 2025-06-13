import datetime

def calculate_age():
    birth_info = input("Введите свою дату рождения (ГГГГ.ММ.ДД): ")
    birth_date = datetime.datetime.strptime(birth_info, "%Y.%m.%d").date()
    today = datetime.date.today()
    age_days = (today - birth_date).days
    years = age_days // 365
    print(f'Вам {years} лет')

calculate_age()


from datetime import datetime, date

def days_until_birthday():
    birth_str = input("Введите дату рождения (ГГГГ.ММ.ДД): ")
    birth_date = datetime.strptime(birth_str, "%Y.%m.%d").date()

    today = date.today()

    next_birthday = date(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

    days_left = (next_birthday - today).days

    print(f"До следующего дня рождения осталось {days_left} дней.")

days_until_birthday()


from datetime import datetime

def datetime_meeting():
    meeting_str = input("Введите дату и время встречи (ГГГГ-ММ-ДД ЧЧ:ММ): ")
    meeting_dt = datetime.strptime(meeting_str, "%Y-%m-%d %H:%M")
    
    now = datetime.now()
    
    diff = meeting_dt - now
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    
    print(f"До встречи осталось {diff.days} дней, {hours} часов, {minutes} минут.")

datetime_meeting()


from datetime import datetime
import pytz

def time_converter():
    time_str = input("Введите дату и время (ГГГГ-ММ-ДД ЧЧ:ММ): ")
    local_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    from_zone = pytz.timezone("Europe/Moscow")
    to_zone = pytz.timezone("Asia/Tashkent")
    local_time = from_zone.localize(local_time)
    converted_time = local_time.astimezone(to_zone)
    print("Время в целевой зоне:", converted_time.strftime("%Y-%m-%d %H:%M"))

time_converter()


import time

seconds = int(input("Введите количество секунд: "))

while seconds > 0:
    print(f"Осталось: {seconds} секунд")
    time.sleep(1)
    seconds -= 1
print("Время вышло!")



def phone_formatter():
    number = input("Введите номер телефона (например: 998901234567): ")

    code_country = number[:3]
    operator = number[3:5]
    first = number[5:8]
    second = number[8:10]
    third = number[10:12]

    formatted = f"+{code_country} {operator} {first}-{second}-{third}"

    print("Отформатированный номер:", formatted)

phone_formatter()


def password_security():
    password = input("Введите пароль: ")
    if len(password) < 8:
        print("Пароль слишком короткий")
        return

    special = "!@#$%^&*()"

    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in special for char in password)

    if has_digit and has_upper and has_special:
        print("Пароль достаточно надёжный")
    else:
        print("Слабый пароль")

password_security()


def word_finder():
    text = input("Введите текст: ")
    word = input("Введите слово для поиска: ")
    if word in text:
        print("Слово найдено")
    else:
        print("Слово не найдено")

word_finder()




import re

def date_extractor():
    text = input("Введите текст: ")
    pattern = r"\d{4}-\d{2}-\d{2}"
    result = re.findall(pattern, text)
    
    if result:
        print("Найденные даты:", result)
    else:
        print("Даты не найдены")

date_extractor()














