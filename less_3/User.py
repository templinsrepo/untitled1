class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def SayFirstName(self):
        print(self.first_name)

    def SayLastName(self):
        print(self.last_name)

    def SayBothName(self):
        print(self.first_name, self.last_name)
