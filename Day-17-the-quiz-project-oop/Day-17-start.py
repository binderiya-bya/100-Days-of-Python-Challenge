# Creating an empty class

class User:
    pass


user_1 = User()
user_1.id = "001"
user_1.username = "bini"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "jack"


# Initializing an object


class User:
    def __init__(self):
        print("A new user is being created...")


user_1 = User()     # everytime an object is created, init function is automatically runs


# Initializing attributes


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = User("001", "angela")    # you have to have two arguments in this case


# Setting default attributes


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "angela")
print(user_1.followers)

# Create a method


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
