#Start the day 17

class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.name = username
        self.followers = 0

user_1 = User("001", "Luciano")
print(user_1.followers)

# def function():
#     pass

# print("hello")

# user_1.id = "001"
# user_1.username = "angela"
# user_2 = User()

# print(user_1.username)
