#password generator 

numbers="0123456789"
letters_lower="abcdefghijklmnopqwrstuvwyxz".lower()
letters_lower="abcdefghijklmnopqwrstuvwyxz".upper()
special="!@#$%¨&*"

def main():
    print('password generator')

    password_length=input("length of the password")
    while password_length.isdigit()==False or int(password_length) <=0:
        print("a password length must be one or more characters long.")
        password_length=input("length of the password")
    password_length=int(password_length)

main()