
#1  function which create a list with key or keys that have the biggest value
def show_keys_with_biggest_value (dictionary):
    return [
            key
            for key, value in dictionary
            if (value == max(dictionary.values()))
            ]
