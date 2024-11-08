import sys, keyboard, time 
from note import Note
from config import configReader
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import ctypes

def set_style(window, DARK_MODE):
    """Styles window and its child widgets"""
    if DARK_MODE == "True":
        DARK_MODE = True
    else:
        DARK_MODE = False
    text_field = window.text_field
    label = window.label
    text_field_style = ("""
        font-size: 48px;
        font-family: "Inconsolata";
        padding: 12px;
        padding-top: 23px;
        border-radius: 5px;
        """)
    label_style = ("""
        font-size: 14px;
        font-family: "Inconsolata";
        border: none;
        background: none;
        """)
    if DARK_MODE:
        text_field_style += """
        background: rgba(57, 62, 70, 90%);
        color: white;
        border: 3px solid #727881;
        """
        label_style += "color: #727881"
    else:
        text_field_style += """
        background: rgba(255, 255, 255, 90%);
        color: black;
        border: 3px solid #979dac;
        """
        label_style += "color: #979dac"

    text_field.setStyleSheet(text_field_style)
    label.setStyleSheet(label_style)

def main():
    config = configReader("config.ini")
    SHOW_KEY = config.SHOW_KEY
    HIDE_KEY = config.HIDE_KEY
    QUIT_KEY = config.QUIT_KEY
    DARK_MODE = config.DARK_MODE
    OBSIDIAN_PATH = config.OBSIDIAN_PATH
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icons/sparkle.png"))

    while True:
        Window = Note(app, HIDE_KEY, QUIT_KEY, SHOW_KEY, OBSIDIAN_PATH) # pass in numeric values of HIDE_KEY and QUIT_KEY for easier checking of key presses
        set_style(Window, DARK_MODE)

        # detect SHOW_KEY press
        pressed = keyboard.read_key()
        if pressed.upper() == SHOW_KEY.upper():
            time.sleep(0.001)
            Window.show()
            Window.activateWindow()
            app.exec()


if __name__ == "__main__":
    main()