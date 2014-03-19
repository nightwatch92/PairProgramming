
class Mail():
    """docstring for Mail"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.container = []

    def get_name(self):

        return self.name

    def get_email(self):
        return self.email
   
    def add_email_name(self, name, email):
        self.container.append([name, email])
        return self.container

    def dictionary(self):
        name_and_email = { self.email : self.name }
        return name_and_email
