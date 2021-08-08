from database import Database as db
from prettytable import PrettyTable
import re


from food import *

class User(db):
    def __init__(self):
        self.Session = []
        self.email = ''
        
    def register(self):
        if self.Session:
            user_list = db.Users
            users = {}
            isUserExist = False
            isPhone = False
            isEmail = False
            isPassword = False

            phoneRegex = '^[0-9]{10}$'
            passRegex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
            emailRegex = '[a-z.@]\.com$'

            name = input('Enter your full name : ')
            phone = input('Enter your contact number : ')
            email = input('Enter your email : ')
            address = input('Enter you address : ')
            password = input('Enter your password (Atleast one small case, upper case, digit, special character, Minimum Length 6-20): ')
            recovery = input('Enter a recovery text (You can change your password with this recovery text only) : ')
            for i in range(len(user_list)):
                if user_list[i]['email']==email:
                    isUserExist=True
                    break
            if(bool(re.search(phoneRegex, phone))):
                isPhone = True
            if(bool(re.search(passRegex, password))):
                isPassword = True
            if(bool(re.search(emailRegex, email))):
                isEmail=True
            if isPhone==True and isPassword==True and isEmail==True and isUserExist==False:
                users['name'] = name
                users['phone'] = phone
                users['email'] = email
                users['address'] = address
                users['password'] = password
                users['recovery'] = recovery   
                db.Users.append(users)            
                print(f'Your account has been created successfully {db.happyMoji}.')
            elif isUserExist==True:
                print('This user already exists, Please try to login or reset the password!')
            elif isPhone==False:
                print('Please enter a valid number!')
            elif isEmail==False:
                print('Please enter a valid email!')
            elif isPassword==False:
                print('Please enter a valid password by checking the note!')
            else:
                print('Except')
        else:
            print('You are already logged in!')

    def login(self):
        if self.Session:
            print('You are already logged in')
        else:
            users = db.Users
            email = input('Enter your email : ')
            password = input('Enter your password : ')

            if users:
                for i in range(len(users)):
                    if users[i]['email']==email:
                        if users[i]['password']==password:
                            self.Session=True
                            self.email = email
                            print(f'Welcome to tastys {db.happyMoji}\n')
                            self.functions_of_users()
                            break
                        else:
                            print('The password you entered is wrong. Please reset the password!')
                            break
                else:
                    print('No such users')
            else:
                print('Currently there are no users')

#This function will display all the activities a user can do
    def functions_of_users(self):
        flag=1
        while flag!=0:
            print('+=========================+')
            print('**   Select any option   **')
            print('+=========================+')
            print('| 1.) Place new order     |')
            print('| 2.) Order History       |')
            print('| 3.) Update Profile      |')
            print('| 4.) Go back             |')
            print('+=========================+')
            option = int(input('Enter the option : '))
            print('\n')
            if option==1:
                self.place_new_order()
            elif option==3:
                self.update_profile()
            elif option==4:
                break
            else:
                print('Invalid input!')

#This function will display all the available food items and will help the user to order
    def place_new_order(self):
        if self.Session:
            food = db.Foods
            cart = []

            if food:
                table = PrettyTable()
                table.field_names = ['Food ID', 'Name', 'Stock', 'Quantity', 'Price', 'Discount', 'Discounted Price']
                food_list = []
                for i in range(len(food)):
                    temp_list = []
                    temp_list.append(food[i]['food_id'])
                    temp_list.append(food[i]['name'])
                    temp_list.append(food[i]['stock'])
                    temp_list.append(food[i]['quantity'])
                    temp_list.append(food[i]['price'])
                    temp_list.append(food[i]['discount'])
                    temp_list.append(food[i]['discounted_price'])
                    food_list.append(temp_list)
                for data in range(len(food_list)):
                    pieces = food_list[data][3]
                    price = food_list[data][4]
                    discount = food_list[data][5]
                    discounted_price = food_list[data][6]
                    if str(pieces).isdigit():
                        food_list[data][3] = str(pieces)+' Pieces'
                    if str(price).startswith('Rs.'):
                        pass
                    else:
                        food_list[data][4] = 'Rs. '+str(price)
                    if str(discount).isdigit():
                        food_list[data][5] = str(discount)+'%'
                    if str(discounted_price).startswith('Rs.'):
                        pass
                    else:
                        food_list[data][6] = 'Rs. '+str(discounted_price)
                    table.add_row(food_list[data])

                print(table)

                food_order = list(map(int, input('Enter food ID : ').split(',')))
                cart = []
                food_id_to_order = []
                for i in food_order:
                    for j in range(len(food)):
                        if food[j]['food_id']==i:
                            stock=food[j]['stock']
                            if stock<1:
                                name = food[j]['name']
                                food_id = food[j]['food_id']
                                print(f'No stock is available for {name} ({food_id})')
                            else:
                                temp_list = []
                                food_id_to_order.append(food[j]['food_id'])
                                temp_list.append(food[j]['food_id'])
                                temp_list.append(food[j]['name'])
                                temp_list.append(food[j]['stock'])
                                temp_list.append(food[j]['quantity'])
                                temp_list.append(food[j]['price'])
                                temp_list.append(food[j]['discount'])
                                temp_list.append(food[j]['discounted_price'])
                                cart.append(temp_list)
                                break
                    else:
                        print(f'{i} is not availabale, Please enter a valid food ID')
                self.cart(cart, food_id_to_order)

            else:
                print('There are no food items to view\n')
        else:
            print('PLease login to view foods\n')
        
    def cart(self, cart, food_id_to_order):
        if cart:
            table = PrettyTable()
            food = db.Foods
            table_list = []
            total_cost = 0
            table.field_names = ['Food ID', 'Food Name', 'Price']
            for i in range(len(cart)):
                temp_list = []
                temp_list.append(cart[i][0])
                temp_list.append(cart[i][1])
                price = 'Rs. '+str(cart[i][6])
                total_cost+=cart[i][6]
                temp_list.append(price)
                table_list.append(temp_list)
            for i in table_list:
                table.add_row(i)
            print(table)
            print('Total : Rs. '+str(total_cost))
            print('+======================+')
            print('|  Confirm your order  |')
            print('+===========+==========+')
            print('| 1.) Yes   | 2.) No   |')
            print('+===========+==========+')
            user_input = int(input('Enter your choice : '))
            if user_input==1:
                for ids in food_id_to_order:       
                    for food_list in range(len(food)):
                        if food[food_list]['food_id']==ids:
                            stock = food[food_list]['stock']
                            food[food_list]['stock']=stock-1
            elif user_input==2:
                del table_list
                print('Your order has been canceled\n')
            else:
                print('Invalid option')

    
#This function will update the users profile except their email
    def update_profile(self):
        if self.Session:
            users = db.Users
            for i in range(len(users)):
                if users[i]['email']==self.email:
                    table = PrettyTable()
                    detail_list = []
                    table.field_names = ['Name', 'Email', 'Contact', 'Recovery Text', 'Address']
                    detail_list.append(users[i]['name'])
                    detail_list.append(users[i]['email'])
                    detail_list.append(users[i]['phone'])
                    detail_list.append(users[i]['recovery'])
                    detail_list.append(users[i]['address'])
                    table.add_row(detail_list)
                    print(table)
                    print('\n')
                    print('+=========================+')
                    print('**   Select any option   **')
                    print('+=========================+')
                    print('| 1.) Name                |')
                    print('| 2.) Contact Number      |')
                    print('| 3.) Recovery text       |')
                    print('| 4.) Address             |')
                    print('| 5.) Go back             |')
                    print('+=========================+')
                    option = int(input('Enter the field number which you need to update : '))
                    print('\n')
                    if option==1:
                        data = input('Enter new name : ')
                        users[i]['name'] = data
                        print('Name has been updated successfully\n')
                        self.update_profile()
                    elif option==2:
                        phoneRegex = '^[0-9]{10}$'
                        data = input('Enter new contact number : ')
                        if (bool(re.search(phoneRegex, data))):
                            users[i]['phone'] = data
                            print('Phone number has been updated successfully\n')
                            self.update_profile()
                        else:
                            print('Enter contact number in correct format!\n')
                    elif option==3:
                        data = input('Enter new recovery text : ')
                        users[i]['recovery'] = data
                        print('Recovery text has been updated successfully\n')
                        self.update_profile()
                    elif option==4:
                        data = input('Enter new address : ')
                        users[i]['address'] = data
                        print('Address has been updated successfully\n')
                        self.update_profile()
                    elif option==5:
                        self.functions_of_users()
                    else:
                        print('Invalid option')

                    break
        else:
            print('Please login to update your profile!')
    
    def reset_password(self):
        if self.Session:
            print('Please logout and try again')
        else:
            users = db.Users
            if users:
                passRegex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
                email = input('Enter your email : ')
                recovery_key = input('Enter your recovery key : ')

                for i in range(len(users)):
                    if users[i]['email'] == email and users[i]['recovery']==recovery_key:
                        new_password = input('Enter your password (Atleast one small case, upper case, digit, special character, Minimum Length 6-20): ')
                        if (bool(re.search(passRegex, new_password))):
                            users[i]['password']=new_password
                            print((f'Password for {email} has been updated successfully'))
                            break
                        else:
                            print('Please enter password in the correct format!')
                            break
                else:
                    print('Email or recovery key is incorrect')

#When this function is called, the session for the current user will end
    def logout(self):
        self.Session=False
        print('Thank you for choosing Tasty\'s\n')
        

a = User()
b = Foods()
a.login()
