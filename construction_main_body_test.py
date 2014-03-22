import mail
import unittest


class Mail(unittest.TestCase):
    """MailerAngel - always there for you"""

    def test_print_all_groups(self):
        mail.lists_name = ['Bonbon']
        self.assertEqual( '[ 1 ] Bonbon', mail.print_all_groups(lists_name))

    def test_get_group(self):
        self.assertEqual( None, mail.get_group())

    def test_add_new_contact(self):
        self.assertEqual( None, mail.add_new_contact())

    def test_create_new_group(self):
        command = tuple('create Boza'.split(" "))
        self.assertEqual( 'New list <Boza> was created', mail.create_new_group(command))

    def test_merge_lists(self):
        self.assertEqual( None, mail.merge_lists())

    def test_export_to_json(self):
        self.assertEqual( None, mail.export_to_json())

if __name__ == '__main__':
    unittest.main()