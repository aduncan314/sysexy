"""
- list/choose available interfaces
- copy sysex file to a machine
"""
import argparse
import importlib

PROGRAMS = {
    'choose': '_choose',
    'send': None,
    'rec': None
}


def send_and_rec():
    args = parse()

    func_module = importlib.import_module(PROGRAMS[args.function])
    func_module.run()


def parse():
    parser = argparse.ArgumentParser('SYSEXY')
    parser.add_argument('function', choices=PROGRAMS)
    parser.add_argument('-c', '--_raw_config', dest='config_path')

    return parser.parse_args()


if __name__ == '__main__':
    send_and_rec()
