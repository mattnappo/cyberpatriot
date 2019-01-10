import sys, subprocess

def CallId(user):
    try:
        id = subprocess.check_output(
            "id " + user,
            shell=True,
            stderr=subprocess.STDOUT
        )
        return str(id)
    except subprocess.CalledProcessError as e:
        # print("[!] fatal error to find id (user does not exist)")
        return ""
class Accounts:
    def __init__(self):
        # Get and store a list of users and user permissions
        # users         = self.__readInput()
        users = [ 
            "matt d",
            "bob d",
            "joey a",
            "janice a"
        ]
        self.users    = [ ]
        self.admins   = [ ]
        self.defaults = [ ]
        self.__parseUsers(users)
        
        # Read and store contents of passwd file
        with open("/etc/passwd", "r") as f:
            self.passwd = f.read()

    # __readInput (private) - Read users input of usernames and permissions
    def __readInput(self):
        users = [ ]
        while True:
            _input = input()
            if _input == "done":
                break
            else:
                users.append(_input)
        return users
    
    # __parseUsers (private) - Parse the list of users inputted by the user
    def __parseUsers(self, users):
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

    """    BEGIN PUBLIC FUNCTIONS    """

    # CheckAllUsersExist - Check that all users exist (both admins and defaults)
    def CheckAllUsersExist(self):
        for user in self.users:
            if not user in self.passwd:
                print("[!] user/admin '" + user + "' does not exist")
            else:
                print("[ ] authorized user/admin '" + user + "' exists")
        print("")

    # CheckAdminsAreAdmin - Check that authorized admins have admin privileges
    def CheckAdminsAreAdmin(self):
        for admin in self.admins:
            id = CallId(admin)
            # id = str(subprocess.check_output(["id", admin]))
            if not "admin" in id or not "sudo" in id:
                print("[!] authorized admin '" + admin + "' does not have admin privileges")
            else:
                print("[ ] authorized admin '" + admin + "' has admin privileges")
        print("")

    # CheckDefaultsAreDefault - Check that default users only have default privileges
    def CheckDefaultsAreDefault(self):
        for default in self.defaults:
            id = CallId(default)
            if "admin" in id or "sudo" in id:
                print("[!] unauthorized user '" + default + "' has admin privileges")
            else:
                print("[ ] default user '" + default + "' does not have admin privileges")
    
    """    END PUBLIC FUNCTIONS    """

def SecureAccounts():
    print("#    ACCOUNTS    #")
    accounts = Accounts()
    accounts.CheckAllUsersExist()
    accounts.CheckAdminsAreAdmin()
    accounts.CheckDefaultsAreDefault()

SecureAccounts()