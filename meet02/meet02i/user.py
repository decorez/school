class User:

    def __init__(self, first_name, last_name, sex, age, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}. The user was a {self.sex} and {self.age} years old.")

    def greet_user(self):
        print(f'Hi {self.first_name}, nice to meet you')

    def increment_login_attempts(self, n=1):
        self.login_attempts += n

    def reset_login_attempts(self):
        self.login_attempts = 0

def main():
    first = User('jose', 'lendy', 'man', '15')
    second = User('christ', 'kevin', 'woman', '15')

    first.describe_user()
    first.greet_user()
    second.describe_user()
    second.greet_user()

    first.increment_login_attempts(2)
    print('The First User already login', first.login_attempts, 'times')
    first.reset_login_attempts()
    print(first.login_attempts)

if __name__ == '__main__':
    main()