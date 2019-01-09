class Accounts:
    def __init__(self, users):
        self.users = users
        with open("/etc/passwd", "r") as f:
            self.passwd = f.read()

    def checkAllUsersExist(self):
        for user in self.users:
            if not user in self.passwd:
                print(user + " not in passwd")
                return False
        return True
        



def test():
    users = [
        "root",
        "user two",
        "user three",
        "user four"
    ]
    accounts = Accounts(users)
    if accounts.checkAllUsersExist():
        print("All users exist")
    else:
        print("A user does not exist")
test()