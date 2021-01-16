
from _configuration import SingleConfig


class Program(object):
    def __init__(self, name: str, config: SingleConfig):
        self._name = name
        self._tokenized_data = []
        self._save_file_path = config.path.joinpath(f"{name}.json")

    def set_program_state(self, msg: str):
        self._tokenized_data = msg.split()

    @property
    def size(self):
        return len(self._tokenized_data)
