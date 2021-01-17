import mido


def run():
    option_list = {'input': mido.get_input_names(),
                   'output': mido.get_output_names()}
    print(f"Running {__name__}")
