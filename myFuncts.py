


def show_keys_with_biggest_value (dictionary):
    return [
            key
            for key, value in dictionary
            if (value == max(dictionary.values()))
            ]
