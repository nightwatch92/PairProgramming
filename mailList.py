class MailList():
    """docstring for MailList"""
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.emails = []

    def get_list_name(self):
        return self.name

    def get_list_index(self):
        return self.index

    def get_list_emails(self):
        return self.emails

    def add_email(self, name, email):
        self.emails.append((name, email))
        return self.emails

    def show_list(self, index):
        #za da se polu4i trqbva container na listove, ot kojto
        #da vzimame lista sys syotvetniq nomer
        message = ""
        pass
        # list1.add_email("Ivo", "ivo@mail.bg")
        # result2 = "[1] Ivo - ivo@mail.bg"