import json
import mailList

class Converter():
    """docstring for Converter"""
    def __init__(self, mailList):
        self.mailList = mailList
        self.mailList_name = mailList.get_list_name()

    def get_file_name(self):
        file_name = self.mailList.get_list_name().replace(" ", "_")
        file_name += ".json"
        return file_name


    def convert_to_dict_list(self):
        self.emails = self.mailList.get_list_emails()
        self.emails_list = []

        #creating a dictionary from every (name, email) and adding it to a list
        for i in range (len(self.emails)):
            email_dict = {}
            email_dict["name"] = self.emails[i][0]
            email_dict["email"] = self.emails[i][1]

            self.emails_list.append(email_dict)
        return self.emails_list


    #list_name, [{name: name1, email: email1}, {name: name2, email: email2}]
    def save_prepare(self):
        content = self.mailList_name
        self.emails_dict = self.convert_to_dict_list()
        content += "\n" + json.dumps(self.emails_dict, indent=4, sort_keys = True, separators=(',', ':'))
        return content

    def save(self):
        file_to_save = open(self.get_file_name(), "w")
        content = self.save_prepare()
        file_to_save.write(content)
        file_to_save.close()