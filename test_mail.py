# test_mail.py

import unittest
import mail

class MailTst(unittest.TestCase):
    """docstring for MailTst"""
    def setUp(self):
        name = "Django"
        email = "Djangoo@yahoo.com"
        self.mail = mail.Mail(name, email)

    def test_name(self):
        self.assertEqual("Django", self.mail.get_name())

    def test_mail(self):
        self.assertEqual("Djangoo@yahoo.com", self.mail.get_email())

    def test_add_email_list(self):
        
        self.assertEqual([['Django','Djangoo@yahoo.com']] , self.mail.add_email_name("Django", "Djangoo@yahoo.com"))
        self.assertEqual([['Django','Djangoo@yahoo.com'], ['Danaila', 'Devitoo@aaa.com']]  , self.mail.add_email_name('Danaila', 'Devitoo@aaa.com'))
        self.assertEqual([['Django','Djangoo@yahoo.com'], ['Danaila', 'Devitoo@aaa.com'], ['Ivan', 'iVan@notMac.com']]  , self.mail.add_email_name('Ivan', 'iVan@notMac.com'))


    def test_dictionary(self):
        self.assertEqual({'Djangoo@yahoo.com': 'Django'},self.mail.dictionary())

if __name__ == '__main__':
    unittest.main()