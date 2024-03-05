import datetime, requests
import speech_recognition


from gtts import gTTS
import os

# ЭТОТ ФАЙЛ БУДЕТ УДАЛЕН, А ВСЕ ФУНКЦИИ ПЕРЕНЕСЕНЫ.
pass

# sr = speech_recognition.Recognizer()
# sr.pause_threshold = 0.5
# r = speech_recognition.Recognizer()
# m = speech_recognition.Microphone(device_index=1)
#
# def create_task():#Создание заметки в todo листе
#     speak('Что добавим в список дел?')
#     query = listen_command()
#     with open('../todo-list.txt', 'a') as file:
#         file.write(f'{query}\n')
#     return f'Задача {query} создана и добавлена в список задач'
#
#
# def weather():
#     speak("В каком городе ты хочешь узнать погоду?")
#     city = listen_command()
#     print(f"[Log] распознан город {city}")
#     return get_weather(city)
#
#
# def get_weather(city, open_weather_token = "e37d54207830a94eee9d3babc8b0d27f"):
#     try:
#         r = requests.get(
#             f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
#         )
#         data = r.json()
#
#         city = data["name"]
#         cur_weather = data["main"]["temp"]
#
#         humidity = data["main"]["humidity"]
#         pressure = data["main"]["pressure"]
#         wind = data["wind"]["speed"]
#         feel = data['main']['feels_like']
#         return (f"Погода в городе: {city}\nТемпература: {cur_weather}° \nОщущается как {feel}°\n"
#               f"Влажность: {humidity}%\nДавление: {pressure} Паскалей \nВетер: {wind} метров в секунду\n")
#
#     except Exception as ex:
#         print(ex)
#         return "Проверьте название города"
#
