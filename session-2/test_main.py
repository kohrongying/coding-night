from unittest import TestCase
import main


class Test(TestCase):
    def test_find_subsequence_trivial(self):
        self.assertEqual(0, main.find_subsequence_count('thoughtworkslikestowritemessycodeandcantidentifycodesmell', ''))

    def test_find_subsequence_t(self):
        self.assertEqual(1, main.find_subsequence_count('thoughtworkslikestowritemessycodeandcantidentifycodesmell', 'lone'))

    def test_find_subsequence_t2(self):
        self.assertEqual(1, main.find_subsequence_count('thoughtworkslikestowritemessycodeandcantidentifycodesmell', 'messy'))

    def test_find_subsequence_f(self):
        self.assertEqual(0, main.find_subsequence_count('thoughtworkslikestowritemessycodeandcantidentifycodesmell', 'badcode'))

    def test_get_weighted_sum(self):
        self.assertEqual(3, main.get_weighted_sum('thoughtworkslikestowritemessycodeandcantidentifycodesmell'))

    def test_get_weighted_sum_2(self):
        self.assertEqual(2, main.get_weighted_sum('thoughtworkslikestoworkaloneandsleep'))

    def test_get_severity_2(self):
        self.assertEqual(2, main.get_severity('thoughtworkslikestoworkaloneandsleep'))

    def test_get_severity_3(self):
        self.assertEqual(3, main.get_severity('thoughtworkslikestowritemessycodeandcantidentifycodesmell'))

    def test_get_severity_NOSEV(self):
        self.assertEqual('NOSEV', main.get_severity('thoughtworkerswritegoodcode'))

    def test_get_weighted_sum_w_good_words(self):
        self.assertEqual(1, main.get_weighted_sum('thoughtworkslikestowritemessycodeandcantidentifycodesmell', True))

    def test_find_subsequence_tdd(self):
        self.assertEqual(2, main.find_subsequence_count('thoughtworkslikestowritemessycodeandcantidentifycodesmell', 'tdd'))
