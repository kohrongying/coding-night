import constants
import argparse


def map_num_to_digit_arr(num):
    d = {
        '1': constants.ONE,
        '2': constants.TWO,
        '3': constants.THREE,
        '4': constants.FOUR,
        '5': constants.FIVE,
        '6': constants.SIX,
        '7': constants.SEVEN,
        '8': constants.EIGHT,
        '9': constants.NINE,
        '0': constants.ZERO
    }
    return d[num]


def add_space(arr):
    return [f'{i} ' for i in arr]


def format_row(arr, width, height):
    formatted = [''] * height

    formatted = ['|' if arr[0] else ' ' for _ in formatted]

    if arr[1]:
        for i in range(len(formatted)):
            if i == len(formatted) - 1:  # if last row
                formatted[i] += '_' * width
            else:
                formatted[i] += ' ' * width
    else:
        formatted = [row + ' ' * width for row in formatted]

    formatted = [row + '|' if arr[2] else row + ' ' for row in formatted]
    return formatted


def print_digit(num, width, height):
    arr = map_num_to_digit_arr(num)
    nested = [format_row(i, width, height) for i in arr]
    return [item for sublist in nested for item in sublist]


def concat_digits(num, width, height):
    final_arr = print_digit(num[0], width, height)
    for digit in str(num)[1:]:
        final_arr = add_space(final_arr)
        arr = print_digit(digit, width, height)
        for i in range(len(arr)):
            final_arr[i] = final_arr[i] + arr[i]
    return final_arr


def print_lcd(num, width, height):
    for i in concat_digits(num, width, height):
        print(i)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print LCD Numbers')
    parser.add_argument('number')
    parser.add_argument('-w', '--width', type=int, default=1)
    parser.add_argument('-ht', '--height', type=int, default=1)
    args = parser.parse_args()

    print_lcd(args.number, args.width, args.height)
