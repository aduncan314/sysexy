import json
from _configuration import SingleConfig


class Program(object):
    def __init__(self, name: str, config: SingleConfig):
        self._name = name
        self._tokenized_data = []
        self._save_file_path = config.path.joinpath(f"{name}.json")

        try:
            self.read()
            self._file_data_hash_value = self._hash_data()
        except FileNotFoundError:
            self._file_data_hash_value = None

        self._from_saved = not (self._file_data_hash_value is None)

    def set_program_state(self, msg: str):
        self._tokenized_data = msg.split()

    @property
    def size(self):
        return len(self._tokenized_data)

    def save(self, overwrite=False):
        """
        Write file with data stored in this instance.

        If a file was found when
        :param overwrite: Allow overwriting file. No effect if no file was found.
        :return:
        """
        if self._from_saved:
            if (not overwrite) and (self._file_data_hash_value != self._hash_data()):
                raise RuntimeError("Trying to overwrite and existing saved program.")

        with self._save_file_path.open('w') as f:
            json.dump(self._serialize(), f, sort_keys=True)

    def read(self):
        """
        Read in program from saved file and store the data in this instance.

        Looks for file at `self._save_file_path` which is determined by `name`
        and `config` at instantiation. Raises if a file is not found.
        """
        with self._save_file_path.open('r') as f:
            self._deserialize(json.load(f))

    def _hash_data(self):
        """Return simple (non secure) hash of program data."""
        return hash(''.join(self._tokenized_data))

    def _serialize(self):
        """Convert stored data into dictionary for storage."""
        return {self._name: {'raw': self._tokenized_data}}

    def _deserialize(self, data: dict):
        """Parse properly formatted dictionary and store in this instance."""
        self._tokenized_data = data[self._name]['raw']
