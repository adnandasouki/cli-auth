from services.auth import Auth
from models.user import User

auth = Auth()
def runApp():
    while (True):
        print('----- authentication system -----')
        print("1.login")
        print("2.signup")
        print("3.exit")

        option = input('select an option: ')

        if option == '1':
            handle_logIn()
        elif option == '2':
            handle_signUp()
        elif option == '3':
            break
        else:
            print('invalid option')
            continue

def handle_logIn():
    print('----- Login -----')
    username = input('username: ')
    password = input('password: ')

    if auth.logIn(username, password):
        handle_account(username)
    else:
        return print('invalid credentials')
            
def handle_signUp():
    print('----- Signup -----')
    username = input('username: ')
    password = input('password: ')

    auth.signUp(User(username, password))

    return print('account created.')

def handle_account(username):
    while (True):
        print(f'----- account -----')
        print('1.settings')
        print('2.signout')

        accountOption = input('select an option: ')
        if accountOption == '1':
            handle_settings(username)
        elif accountOption == '2':
            auth.signOut()
            break

def handle_settings(username):
    while (True):
        print('----- settings -----')
        print('1.change username')
        print('2.change password')
        print('3.delete account')
        print('4.back')

        settingsOption = input('select an option: ')
        if settingsOption == '1':
            username = handle_change_username(username)
        elif settingsOption == '2':
            handle_change_password(username)
        elif settingsOption == '3':
            auth.delete_account(username)
        elif settingsOption == '4':
            break
        else:
            print('invalid option')
            continue

def handle_change_username(username):
    newUsername = input('new username: ')
    updated = auth.change_username(username, newUsername)
    return updated

def handle_change_password(username):
    newPassword = input('new password: ')
    auth.change_password(username, newPassword)