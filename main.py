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
    

    
    
    