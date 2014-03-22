import converter
import mailList
import unittest
import os

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
        self.assertEqual("List_1.json", self.conv1.get_file_name())
        self.assertEqual("Hack_Bulgaria.json", self.conv2.get_file_name())

    def test_convert_to_dict_list(self):
        d = [{"name": "Ivo", "email": "ivo@mail.bg"}, {"name": "Pesho", "email": "pesho@mail.bg"}]
        self.assertEqual(d, self.conv1.convert_to_dict_list())

    """ Written just to see the result, the test itself is not correct
    def test_save_prepare(self):
        result = "[]"
        self.assertEqual(result, self.conv1.save_prepare())
    """

    def test_save_name(self):
        self.conv1.save()
        file_name = self.conv1.get_file_name()

        file = open(file_name, "r")
        contents = file.read()
        file.close()

        lines = contents.split("\n")
        self.assertEqual("List 1", lines[0])
        os.remove(file_name)






if __name__ == '__main__':
    unittest.main()