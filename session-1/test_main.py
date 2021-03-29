from unittest import TestCase
import main
import constants


class Test(TestCase):
  def test_map_num_to_digit_arr(self):
    self.assertEqual(main.map_num_to_digit_arr(1), constants.ONE)

  def test_print_digit_ONE(self):
    arr = main.print_digit(1)
    self.assertEqual(arr, ['   ', '  |', '  |'])

  def test_print_digit_EIGHT(self):
    arr = main.print_digit(8)
    self.assertEqual(arr, [' _ ', '|_|', '|_|'])

  def test_format_row(self):
    self.assertEqual(main.format_row([True, True, True]), '|_|')

  def test_format_row2(self):
    self.assertEqual(main.format_row([False, True, True]), ' _|')

  def test_format_row3(self):
    self.assertEqual(main.format_row([False, False, False]), '   ')

  def test_concat_digits(self):
    self.assertEqual(main.concat_digits(18),
                     [
                       '     _ ',
                       '  | |_|',
                       '  | |_|'
                     ])
