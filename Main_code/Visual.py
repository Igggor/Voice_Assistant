from Graph_predict import *
from main import *
import threading




def main():
    window_width = 300
    window_height = 300
    pyray.init_window(window_width, window_height, 'Голосовой Ассистент')
    pyray.set_exit_key(pyray.KeyboardKey.KEY_F8)
    pyray.set_target_fps(60)
    background_color = colors.BLACK

    buttons = [
        Button(50, 100, 200, 75, 'Micro', 'micro'),
    ]
    micro_text = Text(128, 50, "On", 30, colors.GREEN)
    while not pyray.window_should_close():
        if Settings.micro_changed == False:
            pyray.begin_drawing()
            pyray.clear_background(background_color)
            for i in range(len(buttons)):
                buttons[i].event()
            micro_text.draw()
            pyray.end_drawing()
        else:
            Settings.micro_changed = False
            Settings.micro = not(Settings.micro)
            micro_text.text = "On" if Settings.micro else "Off"
            micro_text.color = colors.GREEN if Settings.micro else colors.RED

if __name__ == '__main__':
    thread1 = threading.Thread(target=main)
    thread1.daemon = True
    thread1.start()
    thread2 = threading.Thread(target=main_bot())
    thread2.daemon = True
    thread2.start()