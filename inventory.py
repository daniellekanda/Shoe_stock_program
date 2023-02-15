#This is a program for Shoe Shop employees.
#Employees can access shoe data for customers or make changes to existing stock. 


#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country 
        self.code = code
        self.product = product 
        self.cost = cost
        self.quantity = int(quantity)

    def get_cost(self):
        cost = self.cost

        return(cost)

    def get_quantity(self):
        quantity = self.quantity
        return(quantity)

    def __str__(self):
    
        output = "==========================\n"
        output += "Product:" + self.product + "\n"
        output += "Quantity:" + str(self.quantity) + "\n"
        output += "Cost:" + self.cost + "\n"
        output += "Code:" + self.code + "\n"
        output += "Country:" + self.country
        
        return(output)

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

#=============Shoe list===========
#This list stores the data for all shoe objects
#This list stores all data for login objects 
shoe_list = []
login_list = []

#==========Functions outside the class==============

#reads all shoe data into a shoe list for manipulation. 
def read_shoes_data():
    try: 
        line_number = [0]
        with open('inventory.txt', 'r+') as f:
            for i, line in enumerate(f):
                if i not in line_number:
                    content = line.strip("\n").split(",")
                    x = Shoe(content[0], content[1], content[2], content[3], content[4])
                    shoe_list.append(x)
    except FileNotFoundError:
        print("This file does not exist.")

#This allows employees to add new shoes to the stock
def capture_shoes():
    new_country = input("Please enter the country: ")
    new_product = input("Please enter the product name: ")
    new_cost = input("Please enter the price of shoe: ")
    new_quantity = input("Please enter the quantity of shoes: ")
    new_code = input("Please enter the shoe code: ")

    new_shoe_object = Shoe(new_country, new_code, new_product, new_cost, new_quantity)

    shoe_list.append(new_shoe_object)

    write_updated_stock()

#alllows employees to view all shoes in stock in the terminal 
def view_all():
    for shoe_object in shoe_list:
        print(shoe_object)

#identifies shoe object with lowestt quantity 
def lowest_quantity():
    lowest_so_far = 100000
    smallest = "name"
    for shoe in shoe_list:
        if shoe.quantity < lowest_so_far:
            lowest_so_far = shoe.quantity
            smallest = shoe
    
    print("The shoe with the lowest stock is: ") 
    print(f"{smallest}")
    print(" ")

    return(smallest)

#asks user how much they want to update stock by, then edits shoe object with new stock amount. 
def reorder_and_update_stock(shoe_object):
    current_stock = 0
    new_stock = 0
    order_request= input("Would you like to increase the stock of the above item?: (y/n)")
    current_stock = shoe_object.quantity
    if order_request == "y":
        restock_size = int(input("Would you like to order 5, 10 or 15 more stock: "))
        if restock_size == 5:
            new_stock = current_stock + 5
            shoe_object.quantity = new_stock 
            print(shoe_object)          
        elif restock_size == 10:
            new_stock = current_stock + 10
            shoe_object.quantity = new_stock   
            print(shoe_object)
        elif restock_size == 15:
            new_stock = current_stock + 15
            shoe_object.quantity = new_stock   
            print(shoe_object)
        else:
            print("Please enter a valid restock size: ")
    elif order_request == "n":
        print("You have not restocked.")
    else:
        print("Please enter a valid answer.")

    return(shoe_object) 

# writes latest shoe object list to text file. 
def write_updated_stock(): 
    with open('inventory.txt', 'w+') as f:
        f.write("Country,Code,Product,Cost,Quantity\n")
        for object in shoe_list:
            f.write("{},{},{},{},{}".format(object.country, object.code, object.product, object.cost, object.quantity))
            f.write("\n")

#main function to identify lowest quantity and automatically restock and rewrite inventory document. Utilising the above functions 
def re_stock():
    smallest_shoe_object = lowest_quantity()
    reorder_and_update_stock(smallest_shoe_object)
    write_updated_stock()

#allows employees to search for shoes by shoe code
def search_shoe():
    user_code = (input("Please enter the shoe code to search: ")).upper()

    for shoe in shoe_list:
        if shoe.code == user_code:
            print(shoe)
        
        else:
            print("This is an invalid code")
    
    return(shoe)

#calculates the stock value of each shoe object. value = cost * quantity
def value_per_item():
    for shoe in shoe_list:
        value = (int(shoe.cost)) * shoe.quantity
        print(shoe)
        print(f"Value: £{value}")

#identifies the shoe with the highest quantity to be marked for sale. 
def highest_qty():
    highest_so_far = 0
    highest = "name"
    for shoe in shoe_list:
        if shoe.quantity > highest_so_far:
            highest_so_far = shoe.quantity
            highest = shoe


    print(" ")
    print("The following item should be put on SALE")
    print(highest)
    print(" ")

    return(highest)

#function to read login data from login text file 
def read_login_data():
    with open('password.txt', 'r+') as f:
        for line in f:
            content = line.strip("\n").split(",")
            x = Passwords(content[0], content[1])
            login_list.append(x)

#requests login information and checks against login list. If login is successful returns access type for user (admin has all access, other users limited)
def login():
    while True:
        print("Welcome to the Danielle Sports Employee Terminal.\nPlease enter your login details to begin.")    
        username_requst = input("Enter username: ").lower()
        password_request = input("Enter password: ").lower()

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

#==========Main Menu=============

#reads shoe data into list for manipulation. 
read_shoes_data()

#reads login data from text file into list for manipulation 
read_login_data()

#welcomes user and asks for their name. This can be edited in the future to include permissions for admins.
all_access = login()


while True:
    #main menu that asks user if they want to support a customer or make changes to the stock
    try:
        main_menu = int(input("""-------MENU-------
1. Review stock for customer
2. Make changes to stock.
3. Exit employee terminal
    Number Choice: """))
        
        #Menu option for user supporting a customer. 
        if main_menu == 1:
            while True:
                try:
                    customer_menu = int(input("""
                    ---CUSTOMER MENU---\n1. View all shoes\n2. Search for specific shoe\n3. Back to main menu
                    Number choice: """))
                    #allows user to view all shoes in stock
                    if customer_menu == 1:    
                        view_all()
                    #allows user to search shoes by code
                    elif customer_menu == 2:
                        search_shoe()
                    #returns user to main menu 
                    elif customer_menu == 3:
                        break
                except ValueError:
                    print("Please enter a valid number")
        #Menu option for user making changes to stock 
        elif main_menu == 2 and all_access == 1:
            while True: 
                try:
                    stock_menu = int(input("""
                    ----STOCK MENU----\n1. Reorder specific shoe\n2. Stock value per item\n3. Identify sale stock\n4. Add new shoe to stock \n5. Back to main menu
                    Number choice: """))
                    #Identifies shoe with lowest stock and allows user to update by increments of 5, 10 or 15. 
                    if stock_menu == 1:
                        re_stock()         
                    #calculates value of each shoe object (value = cost * quantity)
                    elif stock_menu == 2:
                        value_per_item()
                    #idenfies shoe with highest stock to be marked as on sale. 
                    elif stock_menu == 3:
                        highest_qty()
                    #allows user to add new shoe to inventory and writes to inventory text file 
                    elif stock_menu == 4:
                        capture_shoes()
                    #returns user to main menu                     
                    elif stock_menu == 5:
                        break
                except ValueError:
                    print("Please enter a valid number")
        #Non-admins cannot access stock changes. Sent back to main menu. 
        elif main_menu == 2 and all_access == 0:
            print("You do not have admin privileges to make stock changes!")
            main_menu
        #exits program 
        elif main_menu == 3:
            print("Goodbye!")
            exit()
    except ValueError:
        print("Please enter a valid number")
    
    




