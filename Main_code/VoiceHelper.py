from GlobalContext import *
from TextProcessor import *
from SpeechTranslator import *
from Functions import *

import sys


class VoiceHelper:
    """
    Главный класс, отвечающий за связь всех элементов приложения
    Singleton - pattern
    """
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(VoiceHelper, cls).__new__(cls)
        return cls.__instance

    # Конструктор.
    # Инициализируются все составные части приложения (классы), а также словарь functions, где в качестве значений
    # хранятся функции из файла Functions.py.

    # В РЕЗРАБОТКЕ, все функции помощника должны быть здесь.
    def __init__(self):
        """
        Конструктор класса
        Инициализируются все составные части приложения (классы), а также словарь functions, где в качестве значений хранятся функции из файла Functions.py
        """
        self.global_context = GlobalContext()
        self.text_processor = TextProcessor(self.global_context.NAME)
        self.speech_translator = SpeechTranslator()

        self.functions = {
            "time": get_time_now,  # текущее время
            "on": self.set_ON,  # включить
            "off": self.set_OFF,  # выключить (но оставить чувствительной к команде включения,
                                 # т.е приложение остается действующим)
            "full-off": self.exit,  # Деактивация, закрытие приложения
            "date": get_date,  # текущая дата
            "course": get_currency_course  # курс валют
        }

    def set_ON(self):
        """
        Включение голосового помощника
        :return:
        """
        if self.global_context.ON:
            return

        self.speech_translator.speak(self.text_processor.GREETING_PHRASE)
        self.global_context.ON = True

    def set_OFF(self):
        """
        Частичное выключение голосового помощника (спящий режим).
        :return:
        """
        if not self.global_context.ON:
            return

        self.speech_translator.speak(self.text_processor.BYE_PHRASE)
        self.global_context.ON = False

    # Важно! В перспективе здесь не только выход, но, возможно, какое-то сохранение в БД или что-то подобное.
    def exit(self):
        """
        Полное выключение голосового помощника
        :return:
        """
        self.global_context.ON = False
        sys.exit()

        pass

    def listen_command(self):
        """
        Объединение несколько функций и методов. Выполнение работы от приёма и расшифровки голоса до непосредственного выполнения требуемой функции
        :return:
        """
        recognized_query = self.speech_translator.listen_сommand()

        if recognized_query is None:
            return

        if recognized_query == self.speech_translator.RECOGNITION_ERROR_PHRASE:
            self.speech_translator.speak(recognized_query)
            return

        selected_actions = self.text_processor.match_command(recognized_query, self.global_context.ON)

        if selected_actions is None:
            return

        for action in selected_actions:
            self.speech_translator.speak(self.functions[action]())
