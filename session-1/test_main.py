from unittest import TestCase
import main
import constants


class Test(TestCase):
    def test_map_num_to_digit_arr(self):
        self.assertEqual(main.map_num_to_digit_arr('1'), constants.ONE)

    def test_format_row(self):
        self.assertEqual(['|_|'], main.format_row([True, True, True], 1, 1))

    def test_format_row_with_3w_2h(self):
        self.assertEqual([
            '|   |',
            '|___|'
        ], main.format_row([True, True, True], 3, 2))

    def test_format_row_with_2w_3h(self):
        self.assertEqual([
            '|  |',
            '|  |',
            '|__|'
        ], main.format_row([True, True, True], 2, 3))

    def test_format_row2(self):
        self.assertEqual([' _|'], main.format_row([False, True, True], 1, 1))

    def test_format_row2_with_3w_2h(self):
        self.assertEqual([
            '    |',
            ' ___|'
        ], main.format_row([False, True, True], 3, 2))

    def test_format_row_ftf(self):
        self.assertEqual([' _ '], main.format_row([False, True, False], 1, 1))

    def test_print_digit_ONE(self):
        self.assertEqual([
          '   ',
          '  |',
          '  |'
        ], main.print_digit('1', 1, 1))

    def test_print_digit_ONE_with_3w_2h(self):
        self.assertEqual([
          '     ',
          '     ',
          '    |',
          '    |',
          '    |',
          '    |'
        ], main.print_digit('1', 3, 2))

    def test_print_digit_EIGHT(self):
        self.assertEqual([
          ' _ ',
          '|_|',
          '|_|'], main.print_digit('8', 1, 1))

    def test_print_digit_EIGHT_with_3w_2h(self):
        self.assertEqual([
          '     ',
          ' ___ ',
          '|   |',
          '|___|',
          '|   |',
          '|___|'
        ], main.print_digit('8', 3, 2))

    def test_concat_digits_18(self):
        self.assertEqual(main.concat_digits('18', 1, 1),
                         [
                             '     _ ',
                             '  | |_|',
                             '  | |_|'
                         ])

    def test_concat_digits_18_with_3w_2h(self):
        self.assertEqual(main.concat_digits('18', 3, 2),
                         [
                             '           ',
                             '       ___ ',
                             '    | |   |',
                             '    | |___|',
                             '    | |   |',
                             '    | |___|'
                         ])
