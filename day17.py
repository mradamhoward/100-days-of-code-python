class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def print_user_info(self):
        print(f"id: {self.id} username: {self.username} has followers: {self.followers} and is following {self.following}")

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", 'Adam')
user_2 = User("002", 'Kev')
user_1.followers = 2
user_1.follow(user_2) 
user_1.print_user_info()
user_2.print_user_info()