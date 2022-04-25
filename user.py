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
        
        