from lib.models.user import User
from lib.services.auth import Auth

auth = Auth()

def main_screen():
    while (True):
        print('----- auth system -----')
        print("1.login")
        print("2.signup")
        print("3.exit")

        option = input('select an option: ')

        if option == '1':
            login_screen()
        elif option == '2':
            signup_screen()
        elif option == '3':
            break
        else:
            print('--> select a valid option')
            continue

def login_screen():
    print('----- Login -----')
    username = input('username: ')
    password = input('password: ')

    if auth.logIn(username, password):
        account_screen(username)
    # else:
    #     return print('invalid credentials')
            
def signup_screen():
    print('----- Signup -----')
    username = input('username: ')
    password = input('password: ')

    auth.signUp(User(username, password))

    

def account_screen(username):
    while (True):
        print(f'----- {username}\'s account -----')
        print('1.settings')
        print('2.signout')

        option = input('select an option: ')
        if option == '1':
            username = settings_screen(username)
        elif option == '2':
            auth.signOut()
            break

def settings_screen(username):
    while (True):
        print('----- settings -----')
        print('1.change username')
        print('2.change password')
        print('3.delete account')
        print('4.back')

        option = input('select an option: ')
        if option == '1':
            newUsername = input('new username: ')
            username = auth.change_username(username, newUsername)
            return username
        elif option == '2':
            newPassword = input('new password: ')
            auth.change_password(username, newPassword)
        elif option == '3':
            auth.delete_account(username)
        elif option == '4':
            break
        else:
            print('invalid option')
            continue