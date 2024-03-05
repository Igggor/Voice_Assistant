class TextProcessor:
    """
    Класс, отвечающий за сопоставление текста с необходимой командой.
    Singleton - pattern
    """
    __instance = None

    def __new__(cls, name: str):
        if cls.__instance is None:
            cls.__instance = super(TextProcessor, cls).__new__(cls)
        return cls.__instance

    def __init__(self, name: str):
        """
        Конструктор класса.
        Инициалиация словаря доступных команд AVAILABLE_COMMANDS, фразы приветствия (при включении) и прощания (при выключении).
        :param name:
        """
        self.AVAILABLE_COMMANDS = {
            "alias": ("помощник", "бот", "помощь", "ты", "голосовой", name),
            "tbr": ("помоги", "скажи", "расскажи", "покажи", "сколько", "произнеси", "какой"),
            "commands": {
                "here": ["тут", "спишь", "на месте"],
                "thanks": ["спасибо", "благодарю", "благодарствую"],
                "off": ["пока", "отключись", "до свидания"],
                "on": ["привет", "приветствую", "приветик", "ку", "здравия"],
                "time": ["текущее время", "времени", "который час"],
                "weather": ["какая погода", "погода", "погоду"],
                "course": ["евро", "доллар", "курс валют"],
                "features": ['что умеешь']
            }
        }

        self.GREETING_PHRASE = (f"Приветствую, я твой универсальный помощник { name }. Ты можешь узнать о "
                                f"моих возможностях на сайте или просто спросив меня '{ name }, что ты умеешь?'.")

        self.BYE_PHRASE = "Всего доброго, была рада помочь."

    def clean(self, command: str):
        """
        Очистка команды от лишних слов
        :param command: строка с распознанным текстом
        :return: строка с командой
        """
        for item in self.AVAILABLE_COMMANDS['alias']:
            command = command.replace(item, "").strip()
        for item in self.AVAILABLE_COMMANDS['tbr']:
            command = command.replace(item, "").strip()

        return command

    # Важно! В текущем варианте строку можно сопоставить только одной команде. Иначе говоря, одной фразе соответствует
    # ОДНА произвольная команда из этой фразы (та, которая будет найдена первой).
    # *Комментарий автора: будет невероятно удобно, если так и останется)

    # В РАЗРАБОТКЕ.

    # Важно! В этом методе планируется реализовать запись логов
    # (примерный вид: запрос -> что подошло -> доп. информация).
    def match_command(self, command: str, ignore_all: bool):
        """
        Поиск команды в словаре AVAILABLE_COMMANDS
        :param command: строка с командой
        :param ignore_all: Булевая метка. Если True, то учитывается только команда ON
        :return: трока, соответствующая ключу в словаре AVAILABLE_COMMANDS, если команда была успешно найдена, или None в противном случае.
        """
        if not command.startswith(self.AVAILABLE_COMMANDS["alias"]):
            return None

        current_commands = self.clean(command).split()

        if ignore_all:
            for c in current_commands:
                if self.AVAILABLE_COMMANDS["on"].count(c):
                    return "on"

            return None

        for key, values in self.AVAILABLE_COMMANDS["commands"].items():
            for c in current_commands:
                if values.count(c):
                    return key

        return None
