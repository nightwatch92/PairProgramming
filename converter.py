import json
import mailList

class Converter():
    """docstring for Converter"""
    def __init__(self, mailList):
        self.mailList = mailList
        self.mailList_name = mailList.get_list_name()

    def get_file_name(self):
        file_name = self.mailList.get_list_name().replace(" ", "_")
        return file_name

# will be changed in order to look like this:
#[list_name, {name: name1, email: email1}, {name: name2, email: email2}, ..]
    def convert_to_dict(self):
        self.emails = self.mailList.get_list_emails()
        self.emails_dict = {}

        for i in range (len(self.emails)):
            self.emails_dict[self.emails[i][0]] = self.emails[i][1]
        return self.emails_dict



    def save_prepare(self):
        content = ""
        self.emails_dict = self.convert_to_dict()
        content = json.dumps([self.mailList_name, self.emails_dict], indent=4, sort_keys = True, separators=(',', ':'))
        return content