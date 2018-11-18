from unittest import TestCase
from ipynb.fs.full.index import *

class BloomFilterTest(TestCase):

    def test_filterload(self):
        bf = BloomFilter(10, 5, 99)
        item = b'Hello World'
        bf.add(item)
        item = b'Goodbye!'
        bf.add(item)
        expected = '0a4000600a080000010940050000006300000001'
        self.assertEqual(bf.filterload().hex(), expected)
