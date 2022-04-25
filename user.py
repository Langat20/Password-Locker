from credentials import Credential

class User:
    '''
    create a User class that generates new instances of a user 
    '''
    user_list = []
    
    def __init__(self, username, password):
        '''
        initialization method to define user object properties
        args: 
        username: name of the user 
        password: user's password 
        '''
        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        a method to save a new user instance into the user_list 
        '''
        User.user_list.append(self)
        
    @classmethod
    def display_user(cls):
        return cls.user_list 
    
    @classmethod
    def log_in(cls, name, passcode):
        '''
        method to allow a user to login into their account
        
        returns: 
        user credentials if the name and passcode are correct for the user 
        False: for incorrect name or passcode
        '''
        for user in cls.user_list:
            if user.username==name and user.password==passcode:
                return Credential.credential_list
        return False
    
    
        