from user import User

class Admin(User):

    def __init__(self, first_name, last_name, sex, age, privilages='s'):
        super().__init__(first_name, last_name, sex, age, privilages)
        self.privilages = Privilage()

class Privilage():
    def __init__(self):
        self.privilages = ['Can Add Post', 'Can Delete Post', 'Can Ban User']
    
    def show_privilages(self):
        print('an admin can do things like')
        for privilage in self.privilages:
            print(privilage, end=' ')

admin = Admin('jose', 'lendy', 'male', '14')
admin.privilages.show_privilages()