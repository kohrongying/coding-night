import constants
import argparse

def print_digit(num):
    arr = map_num_to_digit_arr(num)
    return [format_row(i) for i in arr]


def format_row(arr):
    char_set = ['|', '_', '|']
    str = ''
    for i, bool in enumerate(arr):
        str += char_set[i] if bool else ' '
    return str


def map_num_to_digit_arr(num):
    d = {
        1: constants.ONE,
        2: constants.TWO,
        3: constants.THREE,
        4: constants.FOUR,
        5: constants.FIVE,
        6: constants.SIX,
        7: constants.SEVEN,
        8: constants.EIGHT,
        9: constants.NINE,
        0: constants.ZERO
    }
    return d[num]


def add_space(arr):
    return [f'{i} ' for i in arr]


def concat_digits(num):
    final_arr = print_digit(int(num[0]))
    for digit in str(num)[1:]:
        final_arr = add_space(final_arr)
        arr = print_digit(int(digit))
        for i in range(len(arr)):
            final_arr[i] = final_arr[i] + arr[i]
    return final_arr


def print_lcd(num):
    for i in concat_digits(num):
        print(i)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print LCD Numbers')
    parser.add_argument('number')
    args = parser.parse_args()
    print(args)
    print_lcd(args.number)