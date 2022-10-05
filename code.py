
client_profiles = {}

def load_data (filename):
    '''
    A function that reads the data file and loads the user profiles into a dictionary.

    Arguments:
        filename: the file name containing the client data.
    
    Returns: 
        client_profiles: a dictionary containing client profiles.
    '''
    infile = open(filename, "r")

    for line in infile:
        line_text = line.replace('\n','').split(',')
        user_name = line_text[0]
        password = line_text[1]
        full_name = line_text[2]
        balance = line_text[3]

        # Creating dictionary
        client_profiles[user_name] = password, full_name, balance

    return client_profiles


def display_info (client_info):
    '''
    A function that uses the client information list to first prompt if the user wants to see the account information. 
    If the user response is yes, it display user full name and account balance

    Arguments:
        client_info: the list contianing the client info for the user who logged in.
    
    Output: 
        Displays user information: full name and account balance        
    '''
    print()
    display_info = input("Would you like to access your account information?\nEnter 'y' for yes and 'n' for no :").lower()
    while display_info != 'y' and display_info != 'n':
        print('invalid entry.')
        print()
        display_info = input("Would you like to access your account information?\nEnter 'y' for yes and 'n' for no :").lower()
    if display_info == 'n':
        print()
        print('Logging out. Good bye.')
        return
    elif display_info == 'y':
        print('****************')
        print('Full Name: ' + client_info[1])
        print('Account Balance: $' + client_info[2] + '.00')
        print('****************')

# def deposit ():
#     deposit_amount = input("This application is currently not accepting deposits in cents.\nPlease only deposit whole dollars. \nEnter the amount you'd like to deposit: ")
#     while not deposit_amount.isnumeric():
#         print('invalid entry.')
#         print()
#         deposit_amount = input("This application is currently not accepting deposits in cents.\nPlease only deposit whole dollars. \nEnter the amount you'd like to deposit: ")


def get_login():
    '''
    A function that prompts for username and password from the user and checks against user dictionary to validate the inouts.
    It only allows maximum of 3 login attempts.
    if the login is successful, it calls the 'display_info' function.    
    '''
    client_info = None
    has_access = False
    count = 0
    while has_access == False:
        if count > 3:
            print('maximum login attempts reached.')
            break
        username_input = input('Username: ').lower()
        password_input = input('Password: ')
        count +=1
        if username_input not in client_profiles:
            print('User name and password not found.')
        else:
            client_info = client_profiles[username_input]
            if client_info[0] != password_input:
                print('User name and password not found.')
            else:
                print() 
                print('LOGIN SUCCESSFUL! Welcome ' + client_info[1] + '.') 
                has_access = True
    if has_access == True:        
        display_info (client_info)


load_data("data.txt")
get_login()
