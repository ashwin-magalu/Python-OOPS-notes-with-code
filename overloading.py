class Account:
    def createAccount(self, name, email, password, mobileno):
        self.name = name
        self.email = email
        self.password = password
        self.mobileno = mobileno

    def createAccount(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def showData(self):
        print(self.name)
        print(self.email)
        print(self.password)
        print(self.mobileno)

account = Account()
account.createAccount("Ashwin", "ashwin@abc.com", "password", 9876543210)
account.showData() 
# error --> TypeError: createAccount() takes 4 positional arguments but 5 were given
"""  The most latest def is run, which only takes 4 parameters, but we are sending 5 parameters. So it won't work. In Java, Function overloading is supported, thus, function will be choosen based on number of arguments if there are multiple functions with same name """