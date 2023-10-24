def is_valid_fmt(input_str):
    states = {0, 1, 2, 3, 4}
    accepting_states = {1}
    transitions = {
        0: {'%': 2},
        2: {'0': 3, '1': 3, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3},
        3: {'0': 3, '1': 3, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3, '.': 4, 'd': 1, 'c': 1, 'f': 1, 's': 1},
        4: {'0': 3, '1': 3, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3},
        1: {}
    }

    current_state = 0
    for char in input_str:
        if current_state in states and char in transitions[current_state]:
            current_state = transitions[current_state][char]
        else:
            return False

    return current_state in accepting_states

# Test cases
test_strings = ["%d", "%123d", "%c", "%", "%x", "%123x", "%fs", "%123fs", "%2f", "%10.2f", "%.1d"]
for test_str in test_strings:
    result = is_valid_fmt(test_str)
    print(f'"{test_str}" is valid: {result}')
