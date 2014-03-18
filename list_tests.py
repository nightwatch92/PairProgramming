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

    def test_add_email(self):
        list1 = list.List(1, "List1")
        self.assertEqual([("Ivo", "ivo@mail.bg")], list1.add_email("Ivo", "ivo@mail.bg"))
        self.assertEqual([("Ivo", "ivo@mail.bg"), ("Pesho", "pesho@mail.bg")], list1.add_email("Pesho", "pesho@mail.bg"))

    def test_show_list(self):
        list1 = list.List(1, "List1")
        result1 = ""
        self.assertEqual(result1, list1.show_list(1))

        list1.add_email("Ivo", "ivo@mail.bg")
        result2 = "[1] Ivo - ivo@mail.bg"
        self.assertEqual(result2, list1.show_list(1))

        list1.add_email("Pesho", "pesho@mail.bg")
        result2 = "[1] Ivo - ivo@mail.bg\n[2] Pesho - pesho@mail.bg"
        self.assertEqual(result2, list1.show_list(1))




if __name__ == '__main__':
    unittest.main()