import os
import speech_recognition
from gtts import gTTS


class SpeechTranslator:
    """
    Класс, отвечающий за перевод СТРОКА <-> ГОЛОС (распознавание и произнесение).
    Singleton - pattern
    """
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SpeechTranslator, cls).__new__(cls)
        return cls.__instance

    def __init__(self, __recognizer_threshold: float = 0.5, __microphone_duration: float = 0.5,
                 __language: str = "ru-RU", __recognizer_error_phrase: str = "Команда не распознана"):
        """
        Конструктор класса.
        Инициализирует с необходимыми параметрами микрофон, распознаватель речи, язык работы.
        :param __recognizer_threshold: float
        :param __microphone_duration: максимальное время прослушивания микрофона
        :param __language: язык ввода
        :param __recognizer_error_phrase: фраза, воспроизводимая при невозможности распознать команду
        """
        self.MICROPHONE = speech_recognition.Microphone(device_index=1)
        self.MICROPHONE_DURATION = __microphone_duration

        self.RECOGNIZER = speech_recognition.Recognizer()
        self.RECOGNIZER.pause_threshold = __recognizer_threshold
        self.RECOGNITION_ERROR_PHRASE = __recognizer_error_phrase

        self.LANGUAGE = __language

    # Важно! Запись логов по задумке должна производиться в классе TextProcessor!
    def listen_сommand(self):
        """
        метод распознавания команды.
        :return: возвращает соответствующее строковое значение,
        или, в случае произвольной ошибки, строку "Команда не распознана".
        """
        try:
            with self.MICROPHONE as sourse:
                self.RECOGNIZER.adjust_for_ambient_noise(source=sourse, duration=self.MICROPHONE_DURATION)
                print("here")

                audio = self.RECOGNIZER.listen(source=sourse, timeout=2)
                query = self.RECOGNIZER.recognize_google(audio_data=audio, language=self.LANGUAGE).lower()

            return query
        except speech_recognition.UnknownValueError:
            return None
        except:
            return self.RECOGNITION_ERROR_PHRASE

    # Важно! Запись логов по задумке должна производиться в классе TextProcessor!
    def speak(self, output_text: str, tempo: float = 1.3):
        """
        Синтезация текста в речь
        :param output_text: текст для синтезации в речь
        :param tempo: скорость воспроизведения
        :return:
        """
        try:
            tts = gTTS(text=output_text, lang=self.LANGUAGE, slow=False, tld="us")
            tts.save('buffer.mp3')

            os.system(f"play buffer.mp3 tempo { tempo }")
        except:
            return None
