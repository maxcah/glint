import os, sys, datetime
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTextEdit, QLabel
from PySide6.QtGui import QFont, QFontDatabase, QIcon

class Note(QWidget):
    """Main widget for the application"""
    def __init__(self, app, HIDE_KEY, QUIT_KEY, SHOW_KEY, OBSIDIAN_PATH):
        super().__init__()
        self.app = app
        self.SHOW_KEY = SHOW_KEY
        self.HIDE_KEY = HIDE_KEY
        self.QUIT_KEY = QUIT_KEY
        self.OBSIDIAN_PATH = OBSIDIAN_PATH
        if not os.path.exists(self.OBSIDIAN_PATH):
            raise FileNotFoundError(f"Obsidian path {self.OBSIDIAN_PATH} does not exist.")

        # Resize window according to screen resolution
        resolution = self.app.primaryScreen().availableGeometry()
        display_width = resolution.width()
        display_height = resolution.height()
        window_width = display_width // 5
        window_height = display_height // 5
        self.resize(window_width, window_height)  
        self.move((display_width - window_width) // 2, (display_height - window_height) // 2)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowTitle("Glint")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon("icons/sparkle.png"))

        # Text field construction
        self.text_field = QTextEdit(parent=self)
        QFontDatabase.addApplicationFont("fonts/Inconsolata-VariableFont_wdth,wght.ttf")
        font = self.text_field.font()
        font.setStyleStrategy(QFont.PreferQuality)
        self.text_field.resize(window_width, window_height) # Text field larger than window to remove border styling and premature line breaks

        # Label construction
        self.label = QLabel(parent=self)
        self.label.setText(f"Glint v. 1.0 // CTRL + {self.QUIT_KEY.upper()} to quit | {self.HIDE_KEY.upper()} to close/save | {self.SHOW_KEY.upper()} to show")
        self.label.move(10, 8)

        self.key_to_value = {    
            '`': 96,           
            '1': 49,                  
            '2': 50,                  
            '3': 51,                  
            '4': 52,                  
            '5': 53,                
            '6': 54,               
            '7': 55,               
            '8': 56,                
            '9': 57,              
            '0': 48,              
            '-': 45,           
            '=': 61,            
            'Backspace': 16777219,          
            'Tab': 16777217,                 
            'Q': 81,                 
            'W': 87,                 
            'E': 69,                  
            'R': 82,                  
            'T': 84,                 
            'Y': 89,                 
            'U': 85,                 
            'I': 73,                 
            'O': 79,                 
            'P': 80,                  
            '[': 91,        
            ']': 93,       
            '\\': 92,          
            'A': 65,                  
            'S': 83,                  
            'D': 68,                 
            'F': 70,                 
            'G': 71,                
            'H': 72,                
            'J': 74,                  
            'K': 75,                 
            'L': 76,                  
            ':': 59,         
            '\'': 39,              
            'Enter': 16777221,            
            'Shift': 16777248,          
            'Z': 90,              
            'X': 88,               
            'C': 67,             
            'V': 86,              
            'B': 66,              
            'N': 78,              
            'M': 77,                
            ',': 44,            
            '.': 46,          
            '/': 47,           
            'Left Ctrl': 17,           
            'Alt': 18,             
            'Space': 32,           
            'CapsLock': 20,       
            'F1': 16777264,           
            'F2': 16777265,            
            'F3': 16777266,           
            'F4': 16777267,          
            'F5': 16777268,           
            'F6': 16777269,           
            'F7': 16777270,           
            'F8': 16777271,          
            'F9': 16777272,          
            'F10': 16777273,          
            'F11': 16777274,           
            'F12': 16777275,          
            'Esc': 27,             
            'LeftArrow': 16777234,        
            'UpArrow': 16777235,          
            'RightArrow': 16777236,     
            'DownArrow': 16777237,        
            'Insert': 16777222,           
            'Delete': 16777223,            
            'Home': 16777232,             
            'End': 16777233,               
            'PageUp': 16777238,            
            'PageDown': 16777239,       
            'NumLock': 144,        
            'ScrollLock': 145,      
            'Pause': 19,            
            'PrintScreen': 44,     
            'Windows': 91,             
            'AltGr': 225,           
            'VolumeUp': 175,         
            'VolumeDown': 174,      
            'Mute': 173,            
            'Play': 250,            
            'Stop': 256,              
            'PrevTrack': 176,         
            'NextTrack': 177,       
            'Esc': 16777216       
            }

    def keyPressEvent(self, event):
        if event.key() == self.key_to_value[self.HIDE_KEY]:
            text = self.text_field.toMarkdown()
            if text.strip() != "":
                cur_time = datetime.datetime.now()
                with open(f"{self.OBSIDIAN_PATH}/{cur_time.year}-{cur_time.month}-{cur_time.day}-{cur_time.second}.md", "w") as f:
                    f.write(text)
            self.app.quit()
        elif event.key() == self.key_to_value[self.QUIT_KEY]: # Quits when CTRL + QUIT_KEY is pressed.
            sys.exit()