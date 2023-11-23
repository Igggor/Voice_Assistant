"""v - 1.7.4"""
from random import randint
import pyautogui as p
from selenium import webdriver
import webbrowser
import subprocess
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests import get
import requests
import pyttsx3, os, time, datetime, requests
import speech_recognition
from prog_searcher import chrome_path


#Инициализация синтезатора и распознование речи
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
speaker = pyttsx3.init()
# speaker.setProperty()
r = speech_recognition.Recognizer()
m = speech_recognition.Microphone(device_index=1)

#Слушаем, что сказал пользователь
def listen_command(listen: bool = True) -> str:
    if (listen == True):
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic, timeout=2)
                query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

            return query
        except speech_recognition.UnknownValueError:
            return 'Команда не распознана'

def create_task():#Создание заметки в todo листе
    speak('Что добавим в список дел?')
    query = listen_command()
    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')
    return f'Задача {query} создана и добавлена в список задач'


#Функция анекдотов (хотел сделать API но мне не понравились анекдоты на том сайте, поэтому пока что массив)
anekdots = ["А вот к нам в студию пришло письмо от Шамиля Прохоровича Кацнельсона из Нигерии...Да уж, как же судьба распорядилась человеком!",
            "С годами становишься всё более мудрым, и мудрость помогает понять, что мудрость не помогает.",
            "Старый еврей говорит жене:- Сара, как только кто-нибудь из нас умрет, я уезжаю в Израиль",
            "«В Прикамье отметят праздник гуся. Гости праздника смогут купить гусиные тушки, одеяла, перины и подушки». Так себе у гуся праздник.",
            "Сегодня Хэллоуин. Приду ненакрашенная",
            "Объявление на пограничном столбе: Товарищи Нарушители! В связи с нехваткой патронов предупредительныевыстрелы в воздух больше не производим!"
            ]
def get_anek():
    return anekdots[randint(0, len(anekdots)-1)]

def date_now():
    now = datetime.datetime.now()
    hour = str(now.hour)
    minutes = str(now.minute)
    return (f"Сейчас {hour}:{'0' * (2 - len(minutes))}{minutes}")

#Функция tts
def speak(sth):
    print(f"[log] said: {sth}")
    speaker.say(sth)
    speaker.runAndWait()
    speaker.stop()



def thanks():
    n = randint(0, 3)
    print(n)
    match n:
        case 0: return "Всегда пожалуйста"
        case 1: return "Пожалуйста"
        case 2: return "Был рад помочь"
        case 3: return "Не за что"



def curs():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    usd = round(data['Valute']['USD']['Value'], 2)
    euro = round(data['Valute']['EUR']['Value'], 2)
    usd_rub = int(usd)
    usd_kop = int(round(usd - int(usd), 2) * 100)
    euro_rub = int(euro)
    euro_kop = int(round(euro - int(euro), 2) * 100)
    return  (f"Курс валют сейчас:\n"
          f"Доллар можно купить за {usd_rub} {sclon(usd_rub, 'rub')} {usd_kop} {sclon(usd_kop, 'kop')}.\n"
          f"Евро можно купить за {euro_rub} {sclon(euro_rub, 'rub')} {euro_kop} {sclon(euro_kop, 'kop')}.\n"
          )



def greeting():
    n = randint(0, 5)
    match n:
        case 0: return "Приветик"
        case 1: return "Привет"
        case 2: return "Дароу"
        case 3: return "Ку"
        case 4: return "Привет, что такое?"
        case 5: return 'Приветcтвую тебя!'





def weather():
    speak("В каком городе ты хочешь узнать погоду?")
    city = listen_command()
    print(f"[Log] распознан город {city}")
    return get_weather(city)



def get_weather(city, open_weather_token="e37d54207830a94eee9d3babc8b0d27f"):


    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        feel = data['main']['feels_like']

        return (f"Погода в городе: {city}\nТемпература: {cur_weather}° \nОщущается как {feel}°\n"
              f"Влажность: {humidity}%\nДавление: {pressure} Паскалей \nВетер: {wind} метров в секунду\n"
              )

    except Exception as ex:
        print(ex)
        return("Проверьте название города")


def sclon(a, txt):
    if(txt == "rub"):
        if (a // 10 != 1) and (a % 10 == 1):
            return ("Рубль")
        elif (a // 10 != 1) and (a % 10 == 2 or a % 10 == 3 or a % 10 == 4):
            return ("Рубля")
        elif (a // 10 != 1) and (a % 10 == 5 or a % 10 == 6 or a % 10 == 7 or a % 10 == 8 or a % 10 == 9 or a % 10 == 0):
            return (("Рублей"))
        else:
            return (("Рублей"))
    if (txt == "kop"):
        if (a // 10 != 1) and (a % 10 == 1):
            return ("Копейку")
        elif (a // 10 != 1) and (a % 10 == 2 or a % 10 == 3 or a % 10 == 4):
            return ("Копейки")
        elif (a // 10 != 1) and (a % 10 == 5 or a % 10 == 6 or a % 10 == 7 or a % 10 == 8 or a % 10 == 9 or a % 10 == 0):
            return (("Копеек"))
        else:
            return (("Копеек"))



def clava():
    p.hotkey('shift', 'alt')
    return "язык ввода изменен"

def sound_lvl():
    speak("Какую громкость вы хотите поставить")
    x = int(listen_command())
    p.press('volumedown', presses=100)
    p.press('volumeup', presses = x // 2)
    return f'Установлена громкость {x}'

#Открытие браузера Google_Chrome
def chrome() -> str:
    ch = subprocess.Popen(chrome_path)
    ch = subprocess.Popen(chrome_path)
    ch.poll()
    return "Открыт браузер хром"


def open_link(what):
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    if ("в youtube видео" in what or "в ютубе видео" in what or "на ютубе видео" in what or "на youtube видео" in what or "видео на ютубе" in what or "на ютуби видео" in what or "видео на ютуби" in what):
        webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={what.replace("в youtube видео", "").replace("в ютубе видео", "").replace("на ютубе видео", "").replace("на youtube видео", "").replace("видео на ютубе", "").replace("видео на youtube", "").replace("на ютуби видео", "").replace("видео на ютуби", "")}')
        return 'Я открыл ютуб с таким запросом'
    if (what == " telegram"):
        webbrowser.open_new_tab("https://web.telegram.org/z/")
        return "телеграм открыт, пользуйся"
    elif (what == " vk"):
        webbrowser.open_new_tab("https://vk.com/")
        return "вк открыт, потом расскажешь, что там нового в ленте"
    elif (what == " youtube"):
        webbrowser.open_new_tab("https://www.youtube.com/")
        return "ютуб открыт, погнали смотреть"
    else:
        webbrowser.get(using='chrome').open_new_tab(f'https://yandex.ru/search/?text={what}')
    return 'Я открыл запрОс в интернете, тут должен быть ответ'

def reboot_sys():
    print("REBOOTING")
    speak("Система будет перезагружена через 3 секунды")
    time.sleep(3)
    import os
    os.system("shutdown -t 0 -r -f")