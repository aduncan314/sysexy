from configparser import ConfigParser, SectionProxy
from pathlib import Path

import mido

FILENAME = '.sysexy.ini'


class SingleConfig(object):
    NAME_LIST = ['primary', 'secondary', 'number']

    def __init__(self, name: str, conf: SectionProxy):
        self._name = name
        self.path = Path(conf['sysex_path']).expanduser()
        self.port = ':'.join([conf[n] for n in self.NAME_LIST])

        print(mido.get_input_names())
        if not self.is_valid:
            raise RuntimeError(f"{self} is not a valid configuration")

    @property
    def name(self):
        return self._name

    @property
    def is_valid(self) -> bool:
        """True if directory exists and the port can be found by mido."""
        return self.path.is_dir() and (self.port in mido.get_input_names())

    def __str__(self):
        return self.name


class SysExyConfiguration(object):
    def __init__(self, base_path='~'):
        self._path = Path(base_path).expanduser().joinpath(FILENAME)
        self._raw_config = ConfigParser()
        try:
            self._raw_config.read(self._path)
        except FileNotFoundError:
            raise RuntimeError("No configuration file found.")

        self.configs = {name: SingleConfig(name, conf)
                        for name, conf in self._raw_config.items()
                        if name != 'DEFAULT'}

    @property
    def options(self):
        return self.configs.keys()

    def get(self, name: str) -> SingleConfig:
        return self.configs[name]
