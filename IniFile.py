import configparser
import os


class IniFile:
    def __init__(self):
        self.path = 'TestStation.ini'
        if not os.path.exists(self.path):
            self.create_config()

    # def __del__(self):
        # self.ini_file.close()

    def create_config(self):
        _iniParser = configparser.ConfigParser()
        """
        Create section 'Hardware Server'
        """
        _iniParser.add_section("Hardware Server")
        _iniParser.set("Hardware Server", "host", "127.0.0.1")
        _iniParser.set("Hardware Server", "port", "1883")
        _iniParser.set("Hardware Server", "clientID", "")
        """
        Create section 'Authorization'
        """
        _iniParser.add_section("Authorization")
        _iniParser.set("Authorization", "name", "")
        _iniParser.set("Authorization", "password", "")

        """
        Create section 'Protocol'
        """
        _iniParser.add_section("Protocol")
        _iniParser.set("Protocol", "type", "")


        with open(self.path, "w") as f:
            _iniParser.write(f)

    def get_hardwareServerIP(self):
        return self.get_setting('Hardware Server', 'host')

    def set_hardwareServerIP(self, serverIP):
        self.update_setting('Hardware Server', 'host', serverIP)

    def get_port(self):
        return self.get_setting('Hardware Server', 'port')

    def set_port(self, port):
        self.update_setting('Hardware Server', 'port', port)

    def get_clientID(self):
        return self.get_setting('Hardware Server', 'clientID')

    def set_clientID(self, clientID):
        self.update_setting('Hardware Server', 'clientID', clientID)

    def get_name(self):
        return self.get_setting('Authorization', 'name')

    def set_name(self, name):
        self.update_setting('Authorization', 'name', name)

    def get_password(self):
        return self.get_setting('Authorization', 'password')

    def set_password(self, password):
        self.update_setting('Authorization', 'password', password)

    def get_protocol(self):
        return self.get_setting('Protocol', 'type')

    def set_protocol(self, protocol):
        self.update_setting('Protocol', 'type', protocol)


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

