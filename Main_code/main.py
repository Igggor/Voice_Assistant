from funcs import *
from Visual import Settings

"""Инициализация переменных"""
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
speaker = pyttsx3.init()
r = speech_recognition.Recognizer()
m = speech_recognition.Microphone(device_index=1)
is_work = True

with m as source:
    """Слушаем и убираем шум"""
    r.adjust_for_ambient_noise(source)


"""Словарик с командами и основными словами бота, типо небольшая иишка"""
commands_dict = {
    "alias": ('помощник','помоги', "help", "бот", "помощь", "боня", "о'кей" , "окей", "ok", "голосовой"),
    "tbr": ("помоги", 'скажи','расскажи','покажи','произнеси'),
    'commands': {
        "here" : ['тут', 'спишь', 'на месте', 'ты тут'],
        "thanks":["спасибо", "благодарю"],
        'off':['пока', "отключись", "до свидания", "отдыхай", "спи"],
        'greeting': ['привет', 'приветствую'],
        'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
        'date_now': ['текущее время', 'сейчас времени', 'который час'],
        'sound_lvl' : ["поменяй звук", 'уровень звука'],
        'chrome': ['открыть браузер', 'открой браузер', 'открыть интернет', 'открой интернет', 'открой chrome'],
        'clava': ['поменяй язык','смени клавиатуру', 'смени язык', 'смени язык системы', 'измени клавиатуру', 'измени язык', 'измени язык системы', 'изменить клавиатуру', 'изменить язык', 'изменить язык системы'],
        "get_anek": ['анекдот','рассмеши меня','ты знаешь анекдоты'],
        "weather":["какая погода", "погода", "погоду"],
        "curs":["евро", "доллар", "курс валют"],
        "open_link": ['найди'],
        "reboot_sys":["перезагрузи компьютер", "перезагрузи комп", "перезагрузи ноут", "перезагрузи ноутбук"],
        "off_micro": ['выключи микрофон', 'выключи микро', 'не слушай меня', 'включи микрофон', '', '']
    }
}

def off_micro():
    Settings.micro_changed = True
    return "Я тебя пока что не слушаю. Чтобы включить микрофон нажми на кнопку включения в приложении"

def here():
    n = randint(1, 2)
    if n == 1:
        return "Я тут, работаю, тебе помогаю"
    elif n == 2:
        return "Я тут. Жду Вашей команды!"

def off():
    """Отключение бота"""
    global is_work
    is_work = False
    Settings.exit_app()
    exit(0)


def main_bot():
    """Основнй цикл работы ассистента"""
    speak("Приветствую, я голосовой помощник Боня, я готов помогать тебе")
    while(is_work):
        if (Settings.micro):
            query = listen_command()
            Settings.action = True
            if query != 'Команда не распознана':
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
                if 'найди' in cmd or 'открой' in cmd:
                    speak(open_link(cmd.replace('найди', '', 1).replace("открой", '', 1)))
        else:
            time.sleep(1)
        Settings.action = False

if __name__ == '__main__':
    main_bot()