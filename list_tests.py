import list
import unittest

class List_tests(unittest.TestCase):
    """docstring for List"""

    def test_get_list_name(self):
        list1 = list.List(1, "List1")
        self.assertEqual("List1", list1.get_list_name())

    def test_get_list_index(self):
        list1 = list.List(1, "List1")
        self.assertEqual(1, list1.get_list_index())



if __name__ == '__main__':
    unittest.main()