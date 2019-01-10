import sys
class Accounts:
    def __init__(self):
        # Get and store a list of users and user permissions
        users         = self.readInput()
        self.users    = [ ]
        self.admins   = [ ]
        self.defaults = [ ]
        self.parseUsers(users)
        
        # Read and store contents of passwd file
        with open("/etc/passwd", "r") as f:
            self.passwd = f.read()

    # Read users input of usernames and permissions
    def readInput(self):
        users = [ ]
        while True:
            _input = input()
            if _input == "done":
                break
            else:
                users.append(_input)
        return users
        
    def parseUsers(self, users):
        for user in users:
            try:
                raw = user.split(" ")
                if raw[1] == "a":
                    self.admins.append(raw[0])
                elif raw[1] == "d":
                    self.defaults.append(raw[0])
                else:
                    print("parsing error")
                    sys.exit(-1)
                self.users.append(raw[0])
            except:
                print("parsing error")
                sys.exit(-1)

    def checkAllUsersExist(self):
        for user in self.users:
            if not user in self.passwd:
                print(user + " not in passwd")
                return False
        return True

    def checkUsersAdmin(self):
        for user in self.users:
            id = str(subprocess.check_output(["id", user]))
            if "admin" or "sudo" in id:
                print("Unauthorized user " + user + " is admin")
                return False


def test():
    users = [
        "ONE a",
        "TWO a",
        "DEF d",
        "DEF0 d"
    ]
    accounts = Accounts()
    if accounts.checkAllUsersExist():
        print("All users exist")
    else:
        print("A user does not exist")

    print(accounts.users)
    print(accounts.admins)
    print(accounts.defaults)
test()