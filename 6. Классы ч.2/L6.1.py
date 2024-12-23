class UserAccount():
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def chek_password(self, test):
        if test == self.__password:
            return True
        else: return False
obj = UserAccount('Mischa', 'mmm', 'poiuy')
obj.set_password('poiuy1')
print(obj.chek_password('poiuy1'))
