import pyray
from raylib import colors

class Settings:
    micro = True
    micro_changed = False
    def exit_app():
        pyray.close_window()
        exit(0)


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, title: str, action: str):
        self.rect = pyray.Rectangle(x, y, width, height)
        self.title = title
        self.act = action
    def event(self):
        if pyray.gui_button(self.rect, self.title):
            self.action()
    def action(self):
        if(self.act == 'close'):
            Settings.exit_app()
        if(self.act == "micro"):
            Settings.micro_changed = True


class Text:
    def __init__(self, x: int, y: int, text: str, size: int, color: pyray.Color):
        self.rect = pyray.Rectangle(x, y, 0, 0)
        self.text = text
        self.size = size
        self.color = color
    def draw(self):
        pyray.draw_text(self.text, int(self.rect.x), int(self.rect.y), self.size, self.color)
