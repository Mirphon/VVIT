class UserAccount():
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.new_password = new_password
        self.password = self.new_password

    def chek_password(self, test):
        self.test = test
        if self.test == self.password:
            return True
        else: return False
obj = UserAccount('Mischa', 'mmm', 'poiuy')
obj.set_password('poiuy1')
print(obj.chek_password('poiuy1'))