import requests
import time
import random
import pandas as pd


data = pd.read_csv('cancel_algo.csv')
# data.drop("Unnamed: 0", axis=1, inplace=True)

GOOGLE_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdDmCIJgiFmBb44l2e9tNFv8VZSQGu3VAm2wil5LJi83egRqw" # ссылка на форму

URL_RESPONSE = GOOGLE_URL + "/formResponse"
URL_REFERER = GOOGLE_URL + "/viewform" 


user_agent = {"Referer": URL_REFERER,
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}

for index, row in data.iterrows():
    form_data = {
        "entry.555457463": f"{row['Урок']}", # заочка\группа
        "entry.1571577516": f"{row['Ссылка']}", # ссылка
        "entry.304166205": f"{row['ФИ']}", # ФИ преподавателя
        "entry.1710419080": f"{row['Причина']}", # Причина
        "entry.54202260_hour": f"{str(row['Время']).split(':')[0]}", # Часы
        "entry.54202260_minute": f"{str(row['Время']).split(':')[1]}", # Минуты
        "entry.157632028_year": f"{str(row['Дата']).split('.')[2]}", # Год
        "entry.157632028_month": f"{str(row['Дата']).split('.')[1]}", # Месяц
        "entry.157632028_day": f"{str(row['Дата']).split('.')[0]}", # День
    }
    try:
       r = requests.post(URL_RESPONSE, data=form_data, headers=user_agent)
       print(f"Отправлена строка {index + 1}. Статус: {r.status_code}")

       # Случайня задержка
       delay = random.uniform(3, 10)
       time.sleep(delay)
    
    except Exception as e:
        print("----------ERROR--------")
        print(f"Ошибка при отправке строки: {index + 1}: {e}")
        print("----------ERROR--------")
        # Задержка при ошибке
        time.sleep(10)
    
print('Завершено...')