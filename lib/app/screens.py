from models.user import User
from services.auth import Auth
import pwinput
from colorama import Fore, init
import os

init(autoreset=True)
auth = Auth()

def main_screen():
    os.system('cls')
    while (True):
        print('===== Authentication System =====')
        print("1.Sign in")
        print("2.Sign up")
        print("3.Exit")

        option = input('Select an option: ')

        if option == '1':
            login_screen()
        elif option == '2':
            signup_screen()
        elif option == '3':
            os.system('cls')
            break
        else:
            os.system('cls')
            print(Fore.RED + 'select a valid option')
            continue

def login_screen():
    os.system('cls')
    print('===== Login =====')
    username = input('Username: ')
    password = pwinput.pwinput('Password: ', mask='•')

    authenticated, message = auth.signIn(username, password)
    
    if not authenticated:
        print(Fore.RED + message)
        return

    os.system('cls')
    print(Fore.GREEN + message)
    account_screen(username)
            
def signup_screen():
    os.system('cls')
    print('===== Signup =====')
    username = input('Username: ')
    password = pwinput.pwinput('Password: ', mask='•')

    validated, message = auth.signUp(User(username, password))
    
    if not validated:
        print(Fore.RED + message)
        return
    
    os.system('cls')
    print(Fore.GREEN + message)
    account_screen(username)
    
def account_screen(username):
    while (True):
        print(f'===== {username}\'s Account =====')
        print('1.Settings')
        print('2.Sign out')

        option = input('Select an option: ')
        if option == '1':
            isDeleted, username = settings_screen(username)
            if isDeleted:
                break
        elif option == '2':
            message = auth.signOut()
            os.system('cls')
            print(Fore.GREEN + message)
            break

def settings_screen(username):
    os.system('cls')
    while (True):
        print('===== Settings =====')
        print('1.Change username')
        print('2.Change password')
        print('3.Delete account')
        print('4.Back')

        option = input('Select an option: ')
        # change username
        if option == '1':
            os.system('cls')
            newUsername = input('New username: ')
            username_changed, username, message = auth.change_username(username, newUsername)
            if not username_changed:
                os.system('cls')
                print(Fore.RED + message)
                continue
            os.system('cls')
            print(Fore.GREEN + message)
            continue
        # change password
        elif option == '2':
            os.system('cls')
            newPassword = pwinput.pwinput('Password: ', mask='•')
            pass_changed, message = auth.change_password(username, newPassword)
            if not pass_changed:
                os.system('cls')
                print(Fore.RED + message)
                continue
            os.system('cls')
            print(Fore.GREEN + message)
            continue
        # delete account
        elif option == '3':
            isDeleted, message = auth.delete_account(username)
            os.system('cls')
            print(Fore.GREEN + message)
            return isDeleted, username
        # back
        elif option == '4':
            os.system('cls')
            return False, username
        else:
            os.system('cls')
            print(Fore.RED + 'Select a valid option')
            continue