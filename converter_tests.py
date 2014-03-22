import converter
import mailList
import unittest

class Converter_tests(unittest.TestCase):
    """docstring for Converter_tests"""

    def setUp(self):
        #a list with 2 emails
        self.l1 = mailList.MailList(1, "List 1")
        self.l1.add_email("Ivo", "ivo@mail.bg")
        self.l1.add_email("Pesho", "pesho@mail.bg")

        #an empty list
        self.l2 = mailList.MailList(2, "Hack Bulgaria")

        #a list with 1 email
        self.l3 = mailList.MailList(3, "List 1")
        self.l3.add_email("Ivo", "ivo@mail.bg")

        self.conv1 = converter.Converter(self.l1)
        self.conv2 = converter.Converter(self.l2)
        self.conv3 = converter.Converter(self.l3)


    def test_get_file_name(self):
        self.assertEqual("List_1", self.conv1.get_file_name())
        self.assertEqual("Hack_Bulgaria", self.conv2.get_file_name())

    def test_convert_to_dict(self):
        d = {"Ivo": "ivo@mail.bg", "Pesho": "pesho@mail.bg"}
        self.assertEqual(d, self.conv1.convert_to_dict())

    def test_save_prepare(self):
        result = "{}"
        self.assertEqual(result, self.conv1.save_prepare())

        #result = "{\'name\': \'Ivo\', \'email\': \'ivo@mail.bg\'}"
        #self.assertEqual(result, self.conv3.save_prepare())
        

if __name__ == '__main__':
    unittest.main()