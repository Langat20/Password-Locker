from user import User
from credentials import Credential

def create_user(username, password):
    new_user=User(username, password)
    return new_user

def save_user(user):
    '''
    method to save a user account 
    '''
    user.save_user()
    
def check_existing_users(name):
    
    return User.user_exists(name)

def user_log_in(name, passcode):
    
    '''
    Args: 
    name: user account username 
    passcode: user account password 
    '''
    log_in=User.log_in(name, passcode)
    if log_in !=False:
        return User.log_in(name, passcode)
    
def display_users():
    '''
    Method that returns all saved users at a given point in time 
    '''
    return User.display_user()

def create_credential(passcode, name, password):
    
    new_credential = Credential(passcode, name, password)
    return new_credential

def save_credentials(credential):
    credential.save_credential()

def check_existing_credential(name):
    return Credential.credential_exist(name)

def display_credentials(password):
    return Credential.display_credentials(password)

def create_generated_password(name):
    
    password=Credential.generate_password()
    return password

def main():
    '''
    Function to run the accounts safe
    '''
    print('''welcome to password locker app \n
          Use these short codes to navigate through the app.''')
    
    while True:
        
        print('''  Short codes:
              ca-creates a user account \n
              du-displays names of current account and users \n
              lg-to log in to your account \n
              q-quit from the account safe account ''')
        
        #take users short codes inputs
        short_codes =input().lower()
        
        if short_codes =="ca":
            print("User name...")  
            username=input()
            
            print("password") 
            password=input() 
            
            save_user(create_user(username,password))
            
            print("\n")
            print(f"{username} welcome to password locker")
            print("\n")
            
        elif short_codes =="du":
            '''
            Display the names of current users 
            '''
            
            if display_users():
                print("\n")
                print("These are the current registred uders")
                print("-"*10)
                
                for user in display_users():
                    print(f"{user.username}")
                    print("-"*10)
                    
            else:
                print("\n")
                print("Password locker has no existing users, be the first user")
                print("\n")
         
        elif short_codes=="lg":
                print("\n")
                print("Log into your account")
                print("Enter your user name")
                username=input()
                
                print("Enter your account password")
                password=input()
                
                if user_log_in(username,password)==None:
                    print("\n")
                    print("Please try again or create an account")
                    print("\n")
                    
                else:
                    user_log_in(username,password)
                    print("\n")
                    print(f'''{username} welcome to your credentials account \n
                          Use these short codes to navigate around''')
                    
                    while True:
                        '''
                        Loop to run methods once a user logs in 
                        '''
                        print(''' Short Codes: 
                              cc-add an account 
                              dc-display credentials 
                              cg-create a credential with a generated password  
                              ex- exit credentials''')
                        
                        short_codes=input().lower()  
                        if short_codes=="cc":
                        
                            print("\n")
                            print("New credentials")
                            print("-"*10)  
                        
                         
                            print("Name of the credential....")
                            credential_name=input()  
                        
                            print("Credential password")
                            credential_password=input() 
                        
                            #create and save a new credential
                            save_credentials=(create_credential(password, credential_name, credential_password))
                        
                            print("\n")  
                            print(f"credentials for {credential_name} has been successfully created and saved")  
                            print("\n")     
                        
                        elif short_codes=="dc":
                    
                            if display_credentials(password):
                                print("\n") 
                                print(f"{username}\'s credentials")
                                print("-"*10)
                                
                                for credential in display_credentials(password):
                                    print(f"Account......{credential.credential_name}")
                                    print(f"Password.....{credential.credential_password}")
                                    print("-"*10)
                                    
                                else:
                                    print("\n") 
                                    print("You have not added any credentials")
                                    print("\n") 
                
                            elif short_codes=="cg":
                                '''
                                To create a credential with generated password 
                                '''
                                print("\n")
                                print("New credential") 
                                print("-"*10)  
                                
                                print("Name of the credential.....")
                                credential_name=(input)
                                
                                save_credential(Credential(password, credential_name, (create_generated_password(credential_name))))
                                print("\n")
                                print(f"Credentials for {credential_name} have been created and saved") 
                                print("\n")
                                
                            elif short_codes=="ex":
                                print(f"{username}, Thank you for using the password locker")
                                print("\n")
                                break  
                            else:
                                print("\n") 
                                print("Short code does not exist")
                                print("\n")
                    
                    
        elif short_codes=="q":
            '''
            Exit the application 
            '''
            print("\n")
            print("Bye")
            break 
        
        else:
            print("\n")
            print("Please use the indicated short codes")
            print("\n")
                        
        
    
if __name__ == '__main__':
    main()
    
    
    
    