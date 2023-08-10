from user import User

class Admin(User):

    def __init__(self, first_name, last_name, sex, age, privilages='s'):
        super().__init__(first_name, last_name, sex, age, privilages)
        self.privilages = ['Can Add Post', 'Can Delete Post', 'Can Ban Userw']

    def show_privilages(self):
         print('You had the privilages such as', end=' ')

         for privilage in self.privilages:
            print(privilage, end=', ')

admin = Admin('jose', 'lendy', 'male', '14')
admin.show_privilages()