from admin import *

class Tastys(Admin):
    admin = Admin()
    j = 1
    try:
        while j!=0:
            print('+----------+')
            print('|1.| Admin |')
            print('|2.| Users |')
            print('|3.| Exit  |')
            print('+----------+')
            request = int(input('Please select an option : '))
            if request==1:
                i=1
                try:
                    while i!=0:
                        print('+=========================+')
                        print('**   Select any option   **')
                        print('+=========================+')
                        print('| 1.) Admin Login         |')
                        print('| 2.) Add Food Items      |')
                        print('| 3.) View Food Items     |')
                        print('| 4.) Edit Food Items     |')
                        print('| 5.) Delete Food Items   |')
                        print('| 6.) Logout              |')
                        print('+=========================+')
                        user_input = int(input('Please select the field : '))
                        print('\n')
                        if user_input==1:
                            admin.admin_login()
                        elif user_input==2:
                            admin.add_food_items()
                        elif user_input==3:
                            admin.view_food_items()
                        elif user_input==4:
                            admin.edit_food_items()
                        elif user_input==5:
                            admin.delete_food_items()
                        elif user_input==6:
                            admin.admin_logout()
                except:
                    print('No options selected!')
            if request==3:
                j=0
                print('Logging out of tastys')
    
    except:
        print('No option selected! Program exiting Admin...........', end=" ")
        print("\U0001F61F")