# Голосовой ассистент для упрощения работы на компьютере людям с ограниченными возможностями
---

## ВВЕДЕНИЕ
Проблема:
: в наше время люди с ограниченными возможностями здоровья сталкиваются с различными трудностями при использовании компьютеров и мобильных устройств.

Актуальность:
: На данный момент есть множество голосовых ассистентов, работающих с устройством пользователя (компьютером, смартфоном и т.п.), но набор их функций минималистичен – выполняют только простейшие задачи. Предлагаемое решение упростит работу за компьютером пользователям с ограниченными возможностями здоровья за счет полного управления системой с помощью голосовых команд, благодаря которым использование персонального компьютера пользователем станет комфортнее и проще.

Цель работы:
: разработка программы, позволяющей пользователям с ограниченными возможностями здоровья использовать персональный компьютер с помощью голосового управления.

Для достижения поставленной цели при выполнении проекта реализуются следующие основные задачи:
1. Регистрация API токенов для работы с json-объектами в интернете;
2. Разработка программного обеспечения для управления устройством с помощью голоса;
3. Программная разработка алгоритма, позволяющего выполнять различные действия по запросам в интернете;
4. Программная разработка алгоритма, позволяющего выполнять действия с устройством;
5.  Тестирование и отладка разработанной программы;
6.  Подготовка описания и презентационных материалов
---

__Программная реализация__ выполнена с использованием языка программирования Python 3.10 в среде разработки PyCharm. Для тестирования разработанного приложения используется компьютер с операционной системой Linux Debian 11. Программная реализация выполнена с использованием библиотеки SpeechRecognition. Для обработки запросов в интернете использовались библиотеки requests, fuzzywuzzy и BeautifulSoup4. Для обработки и выполнения команд управления устройством использовалась библиотека OS.

Разработка начинается с регистрации API токенов для получения json-объектов из интернета. Такой способ получения данных является достаточно быстрым и слабо загружает поток. Затем выполняется разработка основной функции распознавания речи (см. рис. 1 в Приложении) и озвучивание текста (см. рис. 2 в Приложении) – с использованием библиотеки SpeechRecognition[8]  c открытым исходным кодом, позволяющей с помощью синтезатора речи переводить речь в текст и синтезировать речь из текста. 

Важным действием является создание словаря глобальных команд (см. рис. 3 в Приложении). При его составлении нужно учесть тот факт, что пользователь может произносить одну и ту же команду разными словами. При поступлении голосовой команды от пользователя программа сравнивает команду с командами в словаре с помощью библиотеки нечеткого сравнения fuzzywuzzy, что дает возможность распознавания команды, сказанной разными словами. Если команда есть в словаре команд, то она выполняется как глобальная.

Программная реализация выполнена на основе библиотеки SpeechRecognition с открытым исходным кодом для распознавания речи и конвертации текста в речь с использованием языка программирования Python версии 3, Это позволяет обеспечить, возможность распознавания различных команд и озвучивать ответы, благодаря крупной базе кода. Другим важным преимуществом являются реализованные нейронные сети, благодаря которым происходит обучение ассистента и пополнение словаря команд.
Для обеспечения простоты усовершенствования программного обеспечения приложение разделено на две части:

1. Основной код голосового ассистента;
2. Библиотека со всеми функциями голосового ассистента.
Основной код голосового ассистента – принимает и распознает команды пользователя, реагирует на них и отправляет запросы в библиотеку на выполнение команд.
Библиотека функций голосового ассистента – получает запросы на выполнение команд, выполняет команды и возвращает результат выполненных команд по форме ниже:
    1)  date_now – функция, возвращающая актуальные дату и время благодаря библиотеке datatime;
    2)  curs – “Курс валют” – возвращает актуальный курс валют, благодаря получению json-объекта по     ранее зарегистрированному API токену;
    3)  weather – “Погода на сегодня” –  возвращает погоду на сегодняшний день благодаря получению  json-объекта по ранее зарегистрированному API токену;
    4) sclon – функция, отвечающая за правильное произношение слов (склонение и постановка правильного  ударения);
    5)  new – отвечает за переключение темы приложения (светлая или темная) и обратную связь в случае   возникновения ошибки работы приложения;
    6) news – возвращает актуальные новости по темам и разделам, указанным пользователем;
    7)  Weather_on_time – функция, возвращающая погоду на определенный день или отрезок дней;
    8)    W_os – функция, обеспечивающая управление устройством и выполнение команд на устройстве   (выполняется с помощью библиотеки OS). С помощью данной функции выполняется смена раскладки   клавиатуры, изменение уровня звука системы, и т.п.;
    9)    Inet_finder – функция поиска данных в интернете;
    10) GC – функция разговора с пользователем –  может рассказать анекдоты, поделиться интересными     фактами или же просто поддержать беседу. Обучается автоматически при подключении к сети интернет;
    11) Run – функция запуска различных программ на устройстве пользователя, реализованная с помощью    поиска путей до файла (библиотека OS) и запуска сторонних файлов как подпроцессы (библиотека   subprocess);
    12) play_music –  функция запуска музыки – может запускать как музыку с устройства, так и музыку из     сети интернет. Играет фоном и не мешает работе программы


___
__При дальнейшей доработке проекта__ предполагается добавление следующих дополнительных функций:
- увеличение скорости работы программы;
- добавление графического интерфейса с помощью библиотеки PyQT
- управление экосистемой умного дома;
- роботизация алгоритма (использование роботов для выполнения задач);
- создание полноценного искусственного интеллекта.
