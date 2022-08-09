#Start the day 17

class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Luciano")
print(user_1.followers)

user_2 = User("002", "Carla")
print(user_2.followers)

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)

# def function():
#     pass

# print("hello")

# user_1.id = "001"
# user_1.username = "angela"
# user_2 = User()

# print(user_1.username)
