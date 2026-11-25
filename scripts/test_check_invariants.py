import unittest
from check_invariants import compare

class CheckTests(unittest.TestCase):
    def test_no_change(self):
        result = compare('样本为 30 人 [1]。', '样本包括 30 人 [1]。')
        self.assertTrue(all(not v['removed'] and not v['added'] for v in result.values()))
    def test_numbers(self):
        result = compare('12.5% 和 -3', '15% 和 3')['numbers']
        self.assertEqual(result['removed'], {'12.5%': 1, '-3': 1})
        self.assertEqual(result['added'], {'15%': 1, '3': 1})
    def test_citations(self):
        result = compare('结果 [1–3]，见 [@abc]。', '结果 [2]。')['citations']
        self.assertEqual(result['removed'], {'[1–3]': 1, '[@abc]': 1})
    def test_link_code(self):
        result = compare('`foo` https://example.org/a', '`bar` https://example.org/b')
        self.assertEqual(result['inline_code']['removed'], {'foo': 1})
        self.assertEqual(result['urls']['added'], {'https://example.org/b': 1})
    def test_known_limitation(self):
        result = compare('A 为 3，B 为 4。', 'A 为 4，B 为 3。')
        self.assertTrue(all(not v['removed'] and not v['added'] for v in result.values()))

if __name__ == '__main__':
    unittest.main()
