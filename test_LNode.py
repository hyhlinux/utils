import unittest
from unittest import TestCase
from ulnode import LNode


class TestLNode(TestCase):
    def test_create(self):
        n = LNode(3, None)
        self.assertEqual(n.elem, 3)
        self.assertEqual(n.next, None)
    pass
#
#
if __name__ == '__main__':
    unittest.main()
