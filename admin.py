from database import Database as db
from prettytable import PrettyTable
from datetime import date
from food import *
import re

class Admin(db):
    admin = [{'Username': 'admin', 'Password': 'admin'}]
    Session = False

#For adding food items
    def add_food_items(self):
        if self.Session:
            id = db.FoodID#1000
            food = db.Foods
            foodDict = {}

            isQuantity = True
            isPrice = False
            isDiscount = False
            isStock = False
            quantityRegex = '((ml)|(gm)|[0-9])$'

            name = input('Enter food name : ')
            quantity = input('Enter quantity (gm, ml or only digits for pieces) : ')
            price = input('Enter price of the food : ')
            disc = input('Enter discount (as digits only) : ')
            stock = input('Enter no of stocks : ')

            if (bool(re.search(quantityRegex, quantity))==False):
                isQuantity = False
            if price.isdigit():
                isPrice = True
            if disc.isdigit():
                isDiscount = True
            if stock.isdigit():
                isStock = True
            
            if isQuantity is True and isQuantity is True and isPrice is True:
                discount = int(price)-((int(disc)*int(price))/100)
                foodDict['food_id'] = db.FoodID
                foodDict['name'] = name
                foodDict['quantity'] = quantity
                foodDict['price'] = price
                foodDict['discount'] = disc
                foodDict['discounted_price'] = discount
                foodDict['stock'] = stock

                db.Foods.append(foodDict)
                print(f'Successfully added to stock with {id} id\n')
                db.FoodID+=1
            elif isQuantity==False:
                print('You have entered wrong quantity. Please enter quantity in (gm, ml or only digits for pieces!)\n')
            elif isPrice==False:
                print('You have entered wrong price. Please enter only in digits!\n')
            elif isDiscount==False:
                print('You have entered wrong discount. Please enter only in digits!\n')
            elif isStock==False:
                print('You have entered stock in wrong format. Please enter only in digits!\n')
        else:
            print('Please login to add food items.\n')

#For viewing all food items in stock
    def view_food_items(self):
        if self.Session:
            food = db.Foods
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
            else:
                print('There are no food items to view\n')
        else:
            print('PLease login to view foods\n')

#For editing the foods
    def edit_food_items(self):
        if self.Session:
            food = db.Foods
            if food:
                food_id = 0
                quantityRegex = '((ml)|(gm)|[0-9])$'

                try:
                    food_id = int(input('Enter food ID to edit : '))
                    for i in range(len(food)):
                        if food_id == food[i]['food_id']:
                            print('Please select the field which you need to change')
                            print('1. Name\n2. Stock\n3. Quantity\n4. Price\n5. Discount')
                            field = int(input('Enter the field which you want to change : '))
                            if field==1:
                                name = input('Update food item name : ')
                                print('\n')
                                food[i]['name']=name
                                print('Food item\'s name is updated successfully \n')
                            elif field==2:
                                stock = input('Update stock : ')
                                print('\n')
                                if stock.isdigit():
                                    food[i]['stock']=stock
                                    print('Food item\'s stock is updated successfully \n')
                                else:
                                    print('Please enter a valid stock!\n')
                            elif field==3:
                                quantity = input('Enter new quantity (gm, ml or only digits for pieces) : ')
                                print('\n')
                                if (bool(re.search(quantityRegex, quantity))==True):
                                    food[i]['quantity']=quantity
                                    print('Food item\'s quantity is updated successfully \n')
                                else:
                                    print('You have entered wrong quantity. Please enter quantity in (gm, ml or only digits for pieces!)\n')
                            elif field==4:
                                price = input('Enter new price (only in digits): ')
                                print('\n')
                                if price.isdigit():
                                    food[i]['price']=price
                                    print('Food item\'s price is updated successfully \n')
                                else:
                                    print('You have entered wrong price. Please enter only in digits!\n')
                            elif field==5:
                                disc = input('Enter new discount (only in digits): ')
                                print('\n')
                                if disc.isdigit():
                                    price = food[i]['price']
                                    discount = int(price)-((int(disc)*int(price))/100)
                                    food[i]['discount']=disc
                                    food[i]['discounted_price']=discount
                                    print('Food item\'s price is updated successfully \n')
                                else:
                                    print('You have entered wrong discount. Please enter only in digits!\n')
                            else:
                                print('Invalid option\n')
                            break

                    else:
                        print('There are no food items with this ID\n')
                except:
                    print('Please enter a valid food ID\n')

            else:
                print('There are no food items\n')
        else:
            print('Please login to edit food items\n')

#For deletig food items with food ID
    def delete_food_items(self):
        if self.Session:
            food = db.Foods
            if food:
                food_id_to_delete = int(input('Enter the food id to delete : '))
                print('\n')
                for i in range(len(food)):
                    if food[i]['food_id']==food_id_to_delete:
                        del db.Foods[i]
                        print(f'Food item with {food_id_to_delete} is successfully deleted\n')
                        break
                else:
                    print('There are no food items with this id, PLease check from food items\n')
            else:
                print('There are no availabale food items\n')
        else:
            print('Please login to delete food items!\n')

#For admin login
    @classmethod
    def admin_login(cls):
        if cls.Session:
            print('You are already logged in\n')
        else:
            admin=cls.admin
            uname = input('Enter your username : ')
            passwd = input('Enter your password : ')
            for i in range(len(admin)):
                if admin[i]['Username']==uname and admin[i]['Password']==passwd:
                    cls.Session=True
                    print(f'Welcome to Tastys {db.happyMoji}\n')
                else:
                    print(f'Wrong password or username {db.sadMoji}\n')
#For admin logout
    @classmethod
    def admin_logout(cls):
        if cls.Session:
            cls.Session=False
            print('Logged out successfully\n')
        else:
            print('You are not logged in\n')

