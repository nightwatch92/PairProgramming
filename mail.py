
class Mail():
    """docstring for Mail"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):

        return self.name

    def get_email(self):
        return self.email
   
    def add_email_name(self):
        
        add_name = self.name 
        add_email = self.email
        list_of_both = list()
        list_of_both.append(add_name)
        list_of_both.append(add_email)
        return tuple(list_of_both)

    def dictionary(self):
        name_and_email = { self.email : self.name }
        return name_and_email
