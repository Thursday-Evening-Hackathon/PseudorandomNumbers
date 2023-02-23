rule30 = {"111": '0', "110": '0', "101": '0', "000": '0',
    "100": '1', "011": '1', "010": '1', "001": '1'}

def window(iterable, stride=3):
    for index in range(len(iterable) - stride + 1):
        yield iterable[index:index + stride]

initial_state = '00000000000000000000100000000000000000000'

patterns = window(initial_state)
new_state = ''.join(rule30[pat] for pat in patterns)

def generate_pattern(state, rule30):
    for time in range(20):
        print(state)
        patterns = window(state)
        state = ''.join(rule30[pat] for pat in patterns)
        state = '0{}0'.format(state)
    print(state)

generate_pattern(initial_state, rule30)