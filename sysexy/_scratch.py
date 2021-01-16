import json
import time
from pathlib import Path
from typing import Dict

import mido

from program import Program
from _configuration import SysExyConfiguration


def main():
    config = SysExyConfiguration('.')
    mopho_config = config.get('Mopho Keyboard')
    port = mopho_config.port
    messages = _listen(mido.open_input(port))
    p = Program('test', mopho_config)

    for m in messages.values():
        if m.get('sysex'):
            p.set_program_state(m['sysex'])

    _save_sysex(messages, mopho_config.path)


def _listen(in_port) -> Dict[float, dict]:
    start = time.time()
    all_messages = dict()
    while time.time() - start < 10:
        print(time.time())
        msg = in_port.receive()
        all_messages[time.time()] = {msg.type: msg.hex()}

    return all_messages


def _save_sysex(messages: dict, path: Path):
    with path.open('w') as f:
        json.dump(messages, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()
