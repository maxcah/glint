import os, sys, configparser

class configReader:
    def __init__(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Path {filename} does not exist.")

        self.parser = configparser.ConfigParser()
        self.filename = filename
        self.parser.read(self.filename)

        try:
            # keybinds
            self.SHOW_KEY = self.parser.get("KEYBINDS", "SHOW_KEY")
            self.HIDE_KEY = self.parser.get("KEYBINDS", "HIDE_KEY")
            self.QUIT_KEY = self.parser.get("KEYBINDS", "QUIT_KEY")

            # settings
            self.DARK_MODE = self.parser.get("SETTINGS", "DARK_MODE")

            # paths
            self.OBSIDIAN_PATH = self.parser.get("PATHS", "OBSIDIAN_PATH")
            
        except configparser.NoSectionError:
            print("Missing settings in config.ini.")
            sys.exit()
            
