import time
from typing import Dict

import mido

from _configuration import SysExyConfiguration
from program import Program

MOPHO_REQUEST_MSG = mido.Message('sysex', data=[0x01, 0x27, 0x05, 0x02, 0x00])


def main():
    config = SysExyConfiguration('..')
    mopho_config = config.get('MophoKeyboard')
    p = Program('test', mopho_config)

    messages = _listen(mido.open_input(mopho_config.port), mopho_config)

    for m in messages.values():
        if m.get('sysex'):
            p.set_program_state(m['sysex'])

    p.save()


def _listen(in_port, config) -> Dict[float, dict]:
    start = time.time()
    all_messages = dict()
    while time.time() - start < 10:
        if len(all_messages) == 0:
            out_port = mido.open_output(config.port)
            out_port.send(MOPHO_REQUEST_MSG)

        msg = in_port.receive()
        print(time.time())
        all_messages[time.time()] = {msg.type: msg.hex()}

    return all_messages


if __name__ == '__main__':
    main()
