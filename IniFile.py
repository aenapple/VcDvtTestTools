import configparser
import os


class IniFile:
    def __init__(self):
        self.path = 'VcDvtTools.ini'
        if not os.path.exists(self.path):
            self.create_config()

    # def __del__(self):
        # self.ini_file.close()

    def create_config(self):
        _iniParser = configparser.ConfigParser()
        """
        Create section 'Com port'
        """
        _iniParser.add_section("Com port")
        _iniParser.set("Com port", "port", "Com 1")

        with open(self.path, "w") as f:
            _iniParser.write(f)

    def get_ComPort(self):
        return self.get_setting('Com port', 'port')

    def set_ComPort(self, port):
        self.update_setting('Com port', 'port', port)

    def get_setting(self, section, setting):
        _iniParser = configparser.ConfigParser()
        _iniParser.read(self.path)
        value = _iniParser.get(section, setting)
        return value

    def update_setting(self, section, setting, value):
        _iniParser = configparser.ConfigParser()
        _iniParser.read(self.path)
        _iniParser.set(section, setting, value)
        with open(self.path, "w") as f:
            _iniParser.write(f)

