#the mini project 3 paper confused me some so i make some of my own methodology to do project


import datetime
now=datetime.datetime.today()
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

    def __init__(self,contents,total_value):

        self.contents=contents
        self.total_value=total_value # i dont get the meaning of total value, what i refers so i do my own total variable in methods of class Market
    def display_contents(self):     #show what is inside your basket
        Total = 0
        start_number = 1
        print "Your basket contains:"
        for product in market1.users[user_name].basket.contents:
            Total = Total + (market1.inventory[product].price * market1.users[user_name].basket.contents[product])
            print str(start_number) + ".", product, "price=$" + str(market1.inventory[product].price), \
                "amount=" + str(market1.users[user_name].basket.contents[product]), "total=" + str(
                market1.inventory[product].price * market1.users[user_name].basket.contents[product])
            start_number += 1
        print "Total $" + str(Total) + "\n"
        self.show_basket_submenu()
    def show_basket_submenu(self):      #code for basket_submenu


        print "Please Choose an option:\n1.Update amount\n2.Remove an item\n3.Check out\n4.Go back to main menu"
        chose_option = input("Your selection:")
        while chose_option < 0 or chose_option > 4:
            chose_option = input("Re-enter a valid menu item number:")
        if chose_option == 1:

            self.update_item()
            self.show_basket_submenu()
        elif chose_option == 2:
            self.reomve_item()
            self.show_basket_submenu()

        elif chose_option == 3:
            market1.print_receipt()
            market1.check_out()
        elif chose_option == 4:
            market1.show_market_menu(market1.users[user_name])


    def add_item(self):     #this is not in project 2 interface but it is same as with like searching a product
        market1.search(market1.users[user_name])


    def reomve_item(self):
        sub_list_for_user_basket = market1.users[user_name].basket.contents.keys()# this transforms keys as a dictionary
        remove_object = input("Please select which item to remove:")
        while remove_object < 0 or remove_object > len(sub_list_for_user_basket):
            remove_object = input("Re-enter a valid menu item number:")
        del market1.users[user_name].basket.contents[sub_list_for_user_basket[remove_object - 1]]

    def update_item(self):# this code updates number of an item in your basket
        sub_list_for_user_basket = market1.users[user_name].basket.contents.keys()
        change_object = input("Please select which item to change its amount:")
        while change_object < 0 or change_object > len(sub_list_for_user_basket):
            change_object = input("Re-enter a valid menu item number:")
        if 0 < change_object <= len(sub_list_for_user_basket):
            new_amount = input("Please type the new amount:")
            while new_amount > market1.inventory[sub_list_for_user_basket[change_object - 1]].stock_amount:
                print"Sorry! The amount exceeds the limit, Please try again with smaller amount"
                new_amount = input("Amount :")
        market1.users[user_name].basket.contents[sub_list_for_user_basket[change_object - 1]] = new_amount

class User:
    def __init__(self,user_name,user_password,basket):
        self.user_name=user_name
        self.user_password=user_password
        self.basket=basket


class Market:


    def __init__(self):
        global user_name
        self.inventory={"asparagus":InventoryProduct("asparagus",5,10),'broccoli':InventoryProduct("brocoli",6,15),
                        'carrots':InventoryProduct("carrots",7,18),"banana":InventoryProduct("banana",8,10),
                        "berries":InventoryProduct("berries",3,30),"eggs":InventoryProduct("eggs",2,50),
                        'mixed fruit juice': InventoryProduct('mixed fruit juice',8,0),
                        'fish sticks': InventoryProduct('fish sticks',12,25),'ice cream':InventoryProduct('ice cream',6,32),
                        'apple juice': InventoryProduct('apple juice',7,40),'orange juice':InventoryProduct('orange juice',8,30),
                        'grape juice': InventoryProduct('grape juice',9,10)
                        }


        self.users = {'ahmet':User("ahmet",1122,Basket({},0)), 'meryem':User("meryem",3344,Basket({},0))}

    def show_market_menu(self,user):
        print "\nPlease choose one of the following services:\n1. Search for a product\n2. See Basket\n3. Check Out\n4. Logout\n5. Exit\n"
        main_menu_choice = input("Your choice:")
        while main_menu_choice < 1 or main_menu_choice > 5:
            print "Please type a correct main menu number! "
            main_menu_choice = input("Your choice:")
        if main_menu_choice == 1:
            self.search(self.users[user_name])
        elif main_menu_choice == 2:
            Basket.display_contents(market1.users[user_name].basket) #this line calls a method from class Basket
        elif main_menu_choice == 3:
            self.print_receipt()
            self.check_out()
        elif main_menu_choice == 4:
            self.login()
        elif main_menu_choice == 5:
            exit()
    def search(self,user):
        typed = raw_input("What are you searching for?")
        typed = typed.lower()
        start_number = 1
        assigned_number = []

        for property in self.inventory.keys():
            if typed in property:
                assigned_number.append(property)

        while assigned_number == []:
            typed = raw_input("Your search did not match any items. Please try something else (Enter 0 for main menu):")
            if typed == str(0):
                self.show_market_menu(self.users[user_name])

            else:
                for property in self.inventory.keys():
                    if typed in property:
                        assigned_number.append(property)

        print "Found", len(assigned_number), "similar items:"
        for product in assigned_number:
            print str(start_number) + ".", product, str(self.inventory[product].price) + "$"
            start_number += 1

        item_select = input("Please select which item you want to add to your basket (Enter 0 for main menu):")
        if item_select == 0:
            self.show_market_menu(self.users[user_name])
        while item_select > len(assigned_number):
            item_select = input("Re-enter a valid menu item number:")
        if 0 < item_select <= len(assigned_number):
            print "Adding " + assigned_number[item_select - 1] + "."
            chosen_amount = input("Enter amount:")
            while chosen_amount > self.inventory[assigned_number[item_select - 1]].stock_amount:
                print "Sorry! The amount exceeds the limit, Please try again with smaller amount"
                chosen_amount = input("Amount (Enter 0 for main menu):")
                if chosen_amount == 0:
                    self.show_market_menu(self.users[user_name])
            print "Added", assigned_number[item_select - 1], "into your Basket.\nGoing back to main menu..."
            self.users[user_name].basket.contents[assigned_number[item_select-1]] = chosen_amount
            self.show_market_menu(self.users[user_name])
    def update_stock_amount(self,product_name,sold_amount):           #unnecessary code i guess which has same in Basket class above as "update_item"
       Basket.update_item(market1.users[user_name].basket)
    def check_out(self):
        for goods in self.inventory:
            if goods in market1.users[user_name].basket.contents:
                self.inventory[goods].stock_amount = self.inventory[goods].stock_amount - market1.users[user_name].basket.contents[goods]
        self.show_market_menu(self.users[user_name])
    def print_receipt(self):
        print"Processing your receipt..."
        print"******* Sehir Online Market ********"
        print"************************************"
        print"      4444034"
        print"      sehir.edu.tr"
        print "------------------------------------"
        Total = 0
        start_number = 1
        for product in market1.users[user_name].basket.contents:
            Total = Total + (market1.inventory[product].price * market1.users[user_name].basket.contents[product])
            print str(start_number) + ".", product, "price=$" + str(market1.inventory[product].price), \
                "amount=" + str(market1.users[user_name].basket.contents[product]), "total=" + str(
                market1.inventory[product].price * market1.users[user_name].basket.contents[product])
            start_number += 1
        print "------------------------------------"
        print "Total $" + str(Total) + "\n"
        print "------------------------------------"
        print now
        print "Thank You for using our Market!"
    def login(self):
        print "****Welcome to Sehir Online Market****\nPlease log in by providing your user credentials:\n"
        global user_name
        user_name = raw_input("User Name:")
        user_password = input("Password:")


        while user_name not in self.users.keys() or self.users[user_name].user_password != user_password:
            print "Your user name and/or password is not correct. Please try again!\n"
            user_name = raw_input("User Name:")
            user_password = input("Password:")
        print "\nWelcome,", user_name, " Please choose one of the following options \nby entering the corresponding menu number."
        self.show_market_menu(self.users[user_name])


market1=Market() #creating an instance of class Market
market1.login() #code to start method of Market
