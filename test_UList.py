import unittest
from unittest import TestCase
from ulist import UList


class TestUList(TestCase):
    def setUp(self):
        self.ulist = UList()

    def test_is_empty(self):
        self.assertTrue(self.ulist.is_empty())

    def test_len(self):
        self.assertEqual(0, self.ulist.len())

    def test_pre_append(self):
        self.ulist.pre_append(1)
        self.ulist.pre_append(2)
        self.ulist.pre_append(3)
        self.ulist.print_all()
        self.assertEqual(3, self.ulist.len())

    def test_pop(self):
        # if self.ulist.is_empty():
        #     return
        self.ulist.pre_append(1)
        self.ulist.pre_append(2)
        self.ulist.pre_append(3)
        self.test_print_all()
        top = self.ulist.pop()
        self.assertEqual(top, 3)
        top = self.ulist.pop()
        self.assertEqual(top, 2)
        top = self.ulist.pop()
        self.assertEqual(top, 1)
        self.test_print_all()

    def test_append(self):
        # if self.ulist.is_empty():
        #     return
        self.ulist.append(4)
        self.ulist.append(5)
        self.ulist.append(6)
        self.test_print_all()

    def test_pop_last(self):
        while not self.ulist.is_empty():
            self.ulist.pop_last()
        self.test_print_all()
        pass

    def test_find(self):
        def func(elem):
            if elem > 3:
                return True
            else:
                return False

        self.test_pop_last()
        self.ulist.append(1)
        self.ulist.append(3)
        self.ulist.append(5)
        self.ulist.print_all()
        data = self.ulist.find(func=func)
        self.assertEqual(data, 5)

    def test_print_all(self):
        self.ulist.print_all()

    def test_for_each(self):
        def func(elem):
            print("\nfunc:{}".format(elem))

        self.test_pop_last()
        if self.ulist.is_empty():
            self.ulist.append(11)
            self.ulist.append(22)
        self.ulist.print_all()
        self.ulist.for_each(func)

    def test_elements(self):
        def func(elem):
            if elem > 20:
                return True
            else:
                return False
        self.test_pop_last()
        if self.ulist.is_empty():
            self.ulist.append(11)
            self.ulist.append(22)
        # for e in self.ulist.elements():
        #     print("elements:{}".format(e))

        for e in self.ulist.elements(func=func):
            print("elements-func:{}".format(e))


    def tearDown(self):
        self.ulist = None


if __name__ == '__main__':
    unittest.main()
