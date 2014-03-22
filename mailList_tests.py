import mailList
import unittest

class List_tests(unittest.TestCase):
    """docstring for List"""

    def setUp(self):
        self.l1 = mailList.MailList(1, "List1")


    def test_get_list_name(self):
        self.assertEqual("List1", self.l1.get_list_name())


    def test_get_list_index(self):
        self.assertEqual(1, self.l1.get_list_index())


    def test_get_list_emails(self):
        #no contacts in list
        self.assertEqual([], self.l1.get_list_emails())

        #one contact in list
        self.l1.add_email("Ivo", "ivo@mail.bg")
        self.assertEqual([("Ivo", "ivo@mail.bg")], self.l1.get_list_emails())

        #two contacts in list
        self.l1.add_email("Pesho", "pesho@mail.bg")
        self.assertEqual([("Ivo", "ivo@mail.bg"), ("Pesho", "pesho@mail.bg")], self.l1.get_list_emails())


    def test_add_email(self):
        self.assertEqual([("Ivo", "ivo@mail.bg")], self.l1.add_email("Ivo", "ivo@mail.bg"))
        self.assertEqual([("Ivo", "ivo@mail.bg"), ("Pesho", "pesho@mail.bg")], self.l1.add_email("Pesho", "pesho@mail.bg"))


    '''
    def test_show_list(self):
        result1 = ""
        self.assertEqual(result1, self.l1.show_list(1))

        self.l1.add_email("Ivo", "ivo@mail.bg")
        result2 = "[1] Ivo - ivo@mail.bg"
        self.assertEqual(result2, self.l1.show_list(1))

        self.l1.add_email("Pesho", "pesho@mail.bg")
        result2 = "[1] Ivo - ivo@mail.bg\n[2] Pesho - pesho@mail.bg"
        self.assertEqual(result2, self.l1.show_list(1))
    '''


if __name__ == '__main__':
    unittest.main()