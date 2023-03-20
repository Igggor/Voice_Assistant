import random
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
from fuzzywuzzy import fuzz


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
speaker = pyttsx3.init()
r = speech_recognition.Recognizer()
m = speech_recognition.Microphone(device_index=1)

#Слушаем, что сказал пользователь
def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

        return query
    except speech_recognition.UnknownValueError:
        return 'Команда не распознана'

def play_music(play = True):# Проигрование функции, но еще надо дописать

    name = random.choice(os.listdir('D:\Music'))
    song = os.path.join('D:\Music', name)
    from pygame import mixer
    mixer.init()
    mixer.music.load(song)
    if (play):
        mixer.music.set_volume(0.3)
        mixer.music.play()
        return f"Слушаем {name[:-4]}"
    else:
        mixer.music.stop()
        return "Музыка отключена"


def next_track():

    name = random.choice(os.listdir('D:\Music'))
    song = os.path.join('D:\Music', name)
    from pygame import mixer
    mixer.init()
    mixer.music.stop()
    mixer.music.load(song)
    mixer.music.set_volume(0.3)
    mixer.music.play()
    return f"Слушаем следующую композицию {name[:-4]}"


    #os.system('cd H:\Программирование\Python files\VoiceAssestant')
    #return "Не танцуем, я еще не умею включать музыку, извини, но я активно учусь" #f'Танцуем под {random_file.split("/")[-1]} 🔊🔊🔊'

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
    return anekdots[random.randint(0, len(anekdots)-1)]

def date_now():
    now = datetime.datetime.now()
    return ("Сейчас " + str(now.hour) + ":" + str(now.minute))

#Функция tts
def speak(sth):
    print(f"[log] said: {sth}")
    speaker.say(sth)
    speaker.runAndWait()
    speaker.stop()



def thanks():
    n = random.randint(0, 3)
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
    n = random.randint(0, 5)
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


#open_weather_token = "e37d54207830a94eee9d3babc8b0d27f"

def get_weather(city, open_weather_token = "e37d54207830a94eee9d3babc8b0d27f"):


    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        #if weather_description in code_to_smile:
        #    wd = code_to_smile[weather_description]
        #else:
        #    wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
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

def chrome():
    ch = subprocess.Popen(chrome_path)
    ch.poll()
    return "Открыт браузер хром"


def open_link(what="telegram"):
    if (what == "telegram"):
        webbrowser.open_new_tab("https://web.telegram.org/z/")
        return "телеграм открыт, пользуйся"
    elif (what == "vk"):
        webbrowser.open_new_tab("https://vk.com/")
        return "вк открыт, потом расскажешь, что там нового в ленте"

    elif (what == "youtube"):
        webbrowser.open_new_tab("https://www.youtube.com/")
        return "ютуб открыт, погнали смотреть"


#def open(what):
#    pass
#r = 2
#k = 2
#print(r, sclon(r, 'rub'))
#print(k, sclon(k, 'kop'))