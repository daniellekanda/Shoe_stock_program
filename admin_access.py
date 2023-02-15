#=====Class=====
class Passwords:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def get_username(self):
        username = self.username 

        return(username)
    
    def get_password(self):
        password = self.password

        return(password)
    
    def __str__(self):
        output = "Username: " + self.username + "\n"
        output += "Password: " + self.password + "\n"

        return(output)

#=====List======

login_list = []

#=======Functions========

def read_login_data():
    with open('password.txt', 'r+') as f:
        for line in f:
            content = line.strip("\n").split(",")
            x = Passwords(content[0], content[1])
            login_list.append(x)

def login():
    while True:    
        username_requst = input("enter username: ").lower()
        password_request = input("enter password: ").lower()


        for users in login_list:
            if users.username == username_requst and users.password == password_request:
                user_found = True
                break
            else:
                user_found = False

        if user_found == True:
            if username_requst == "admin":     
                user_access = 1
                break
            else:
                user_access = 0
                break
        elif user_found == False:
            print("Your username or password is incorrect. Please try again.")
    
    return(user_access)

#======Login Programe=======

read_login_data() 
all_access = login()

if all_access == 1:
    print("all access")
else:
    print("limited access")
