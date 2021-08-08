from database import Database as db

class Foods(db):
    def __init__(self):
        foodDict = {}
        discount = 196
        foodDict['food_id'] = 1001
        foodDict['name'] = 'Tandoori Chicken'
        foodDict['quantity'] = 4
        foodDict['price'] = 200
        foodDict['discount'] = 2
        foodDict['discounted_price'] = discount
        foodDict['stock'] = 100
        db.Foods.append(foodDict)
        db.FoodID+=1

        foodDict = {}
        discount = 333
        foodDict['food_id'] = 1002
        foodDict['name'] = 'Vegan Burger'
        foodDict['quantity'] = 2
        foodDict['price'] = 350
        foodDict['discount'] = 5
        foodDict['discounted_price'] = discount
        foodDict['stock'] = 0
        db.Foods.append(foodDict)
        db.FoodID+=1

        foodDict = {}
        discount = 960
        foodDict['food_id'] = 1003
        foodDict['name'] = 'Truffle Cake'
        foodDict['quantity'] = '1000gm'
        foodDict['price'] = 1200
        foodDict['discount'] = 20
        foodDict['discounted_price'] = discount
        foodDict['stock'] = 100
        db.Foods.append(foodDict)
        db.FoodID+=1

        foodDict = {}
        discount = 600
        foodDict['food_id'] = 1004
        foodDict['name'] = 'Black Forest'
        foodDict['quantity'] = '500gm'
        foodDict['price'] = 1200
        foodDict['discount'] = 50
        foodDict['discounted_price'] = discount
        foodDict['stock'] = 46
        db.Foods.append(foodDict)
        db.FoodID+=1