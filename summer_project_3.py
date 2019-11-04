class InventoryProduct(object):
    def __init__(self, name, price, stock_amount):
        self.name = name
        self.price = price
        self.stock_amount = stock_amount


class BasketProduct(InventoryProduct):
    def __init__(self, name, price, stock_amount, basket_amount):
        super(BasketProduct,self).__init__(name ,price, stock_amount)
        self.basket_amount = basket_amount




class Basket:
    global product_name
    product_name=""

    def __init__(self,product_name):

        self.contents={product_name:BasketProduct(name="",price=0,stock_amount=0,basket_amount=0)}
        self.total_value=1        #simdilik
    def display_contents(self):
       pass
    def show_basket_submenu(self):
        pass
    def add_item(product):
        pass
    def reomve_item(self):
        pass



class User:
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password=password
        self.basket=Basket(product_name="")

class Market:


    def __init__(self):
        self.inventory={"asparagus":InventoryProduct("asparagus",5,10),'broccoli':InventoryProduct("brocoli",6,15),
                        'carrots':InventoryProduct("carrots",7,18),"banana":InventoryProduct("banana",8,10),
                        "berries":InventoryProduct("berries",3,30),"eggs":InventoryProduct("eggs",2,50),
                        'mixed fruit juice': InventoryProduct('mixed fruit juice',8,0),
                        'fish sticks': InventoryProduct('fish sticks',12,25),'ice cream':InventoryProduct('ice cream',6,32),
                        'apple juice': InventoryProduct('apple juice',7,40),'orange juice':InventoryProduct('orange juice',8,30),
                        'grape juice': InventoryProduct('grape juice',9,10)
                        }


        self.users = {'ahmet':User("ahmet",1122,), 'meryem':User("meryem",3344)}
    def log_in(user):
        global user_name
        user_name = raw_input("User Name:")
        user_password = input("Password:")
        while user_name not in user.users.keys()or user.users[user_name].password !=user_password:
            print "Your user name and/or password is not correct. Please try again!\n"
            user_name = raw_input("User Name:")
            user_password = input("Password:")
        print "\nWelcome,", user_name, " Please choose one of the following options \nby entering the corresponding menu number."
        user.show_market_menu()
    def show_market_menu(user):
        print "\nPlease choose one of the following services:\n1. Search for a product\n2. See Basket\n3. Check Out\n4. Logout\n5. Exit\n"
        main_menu_choice = input("Your choice:")
        while main_menu_choice < 1 or main_menu_choice > 5:
            print "Please type a correct main menu number! "
            main_menu_choice = input("Your choice:")
        if main_menu_choice == 1:
            user.search()
        elif main_menu_choice == 2:
            pass
        elif main_menu_choice == 3:
            pass
        elif main_menu_choice == 4:
            pass
        elif main_menu_choice == 5:
            exit()
    def search(user):
        typed = raw_input("What are you searching for?")
        typed = typed.lower()
        start_number = 1
        assigned_number = []

        for property in user.inventory.keys():
            if typed in property:
                assigned_number.append(property)

        while assigned_number == []:
            typed = raw_input("Your search did not match any items. Please try something else (Enter 0 for main menu):")
            if typed == str(0):
                user.show_market_menu()

            else:
                for property in user.inventory.keys():
                    if typed in property:
                        assigned_number.append(property)

        print "Found", len(assigned_number), "similar items:"
        for product in assigned_number:
            print str(start_number) + ".", product, str(user.inventory[product].price) + "$"
            start_number += 1

        item_select = input("Please select which item you want to add to your basket (Enter 0 for main menu):")
        if item_select == 0:
            user.show_market_menu()
        while item_select > len(assigned_number):
            item_select = input("Re-enter a valid menu item number:")
        if 0 < item_select <= len(assigned_number):
            print "Adding " + assigned_number[item_select - 1] + "."
            chosen_amount = input("Enter amount:")
            while chosen_amount > user.inventory[assigned_number[item_select - 1]].stock_amount:
                print "Sorry! The amount exceeds the limit, Please try again with smaller amount"
                chosen_amount = input("Amount (Enter 0 for main menu):")
                if chosen_amount == 0:
                    user.show_market_menu()
            print "Added", assigned_number[item_select - 1], "into your Basket.\nGoing back to main menu..."
            user.users[user_name].basket.contents[product_name].basket_amount = chosen_amount
            user.show_market_menu()


market1=Market()
market1.log_in()


