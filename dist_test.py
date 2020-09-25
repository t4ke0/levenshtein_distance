import unittest
from typing import NamedTuple
from levedist import Levenshtein


class PairWord(NamedTuple):
    word_one:str
    word_two:str

class TestLeveshteinDist(unittest.TestCase):
    def test_dist(self):
        p1 = PairWord("takeo","makeo")
        p2 = PairWord("sitting","kitten")
        p3 = PairWord("book","back")
        cases = {p1:1,p2:3,p3:2}

        for k,v in cases:
            l = Levenshtein(k,v)
            d = l.distance()
            self.assertEqual(d,cases[PairWord(k,v)])

if __name__ == "__main__":
    unittest.main()

