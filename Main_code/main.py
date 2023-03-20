from funcs import *
#Инициализация переменных
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
speaker = pyttsx3.init()
r = speech_recognition.Recognizer()
m = speech_recognition.Microphone(device_index=1)
is_work = True


#Слушаем и убираем шум
with m as source:
    r.adjust_for_ambient_noise(source)


#Словарик с командами и основными словами бота, типо небольшая иишка
commands_dict = {
    "alias": ('помощник','помоги', "help", "бот", "помощь", "ты", "игорь","о'кей" , "окей", "ok", "голосовой"),
    "tbr": ("помоги", 'скажи','расскажи','покажи','сколько','произнеси'),
    'commands': {
        "here" : ['тут', 'спишь', 'на месте'],
        "thanks":["спасибо", "благодарю"],
        'off':['пока', "отключись", "до свидания"],
        'greeting': ['привет', 'приветствую'],
        'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
        'date_now': ['текущее время','сейчас времени','который час'],
        'off_music': ['выключи музыку', 'отключи музыку'],
        'play_music': ['включи музыку', 'дискотека'],
        'sound_lvl' : ["поменяй звук", 'уровень звука'],
        'chrome': ['открыть браузер', 'открой браузер', 'открыть интернет', 'открой интернет', 'открой chrome'],
        'clava': ['поменяй язык','смени клавиатуру', 'смени язык', 'смени язык системы', 'измени клавиатуру', 'измени язык', 'измени язык системы', 'изменить клавиатуру', 'изменить язык', 'изменить язык системы'],
        "anek": ['анекдот','рассмеши меня','ты знаешь анекдоты'],
        "weather":["какая погода", "погода", "погоду"],
        "curs":["евро", "доллар", "курс валют"]
    }
}
def here():
    return "Я тут, работаю, тебе помогаю"


def anek():
    n = get_anek()
    return n

def off_music():
    play_music(play=False)
    return "Музыка выключена"


#Отключение бота
def off():
    global is_work
    is_work = False
    return "Я был рад помогать тебе, жду возможности помочь ещё"


#Основнй цикл работы ассистента
speak("Приветствую, я голосовой помощник Игорь, я готов помогать тебе")
while(is_work):
    query = listen_command()
    print(f"[Log] Распознано: {query}")
    if query.startswith(commands_dict["alias"]):
    # обращаются к боту
        cmd = query
        #Удаляем обраение к ассистенту
        for x in commands_dict['alias']:
            cmd = cmd.replace(x, "").strip()
        #Удаляем действие
        for x in commands_dict['tbr']:
            cmd = cmd.replace(x, "").strip()
        #Получаем команду
        for k, v in commands_dict['commands'].items():
            if cmd in v:
                speak(globals()[k]())
                break