import string 
from random import choice
'''
import string and random modules into the file
'''
class Credential:
    '''
    class blueprint to creat instances of credentials
    '''
    
    credential_list = []
    def __init__(self, user_name, user_password, credential_name, credential_password):
        
        '''
        Args:
            user_name: name of the user
            user_password: user login password
            credential_name: user account's name 
            credential_password: user account's password
        '''
        self.user_name = user_name
        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password
    def save_credential(self):
        Credential.credential_list.append(self)
        
    @classmethod
    def generate_password(cls):
        '''
        method to generate a random passcode
        '''
        size=6
        
        passcode=string.ascii_uppercase+string.digits+string.ascii_uppercase
        
        #creating the login password
        password=''.join(choice(passcode) for num in range(size))
        
        return password
    @classmethod
    def display_credentials(cls, password):
        
        #generate an empty user credential list
        user_credential_list=[]
        
        '''
        loop through the the credential list to get credentials of a single user
        '''
        for credential in cls.credential_list:
            if credential.user_password==password:
                user_credential_list.append(credential)
        return user_credential_list
    
    @classmethod 
    def credential_exist(cls, name):
        '''
        A method to check if a credential exists in the credential list 
        '''
        for credential in cls.credential_list:
            if credential.credential_name == name:
                return True
        return False
    
    @classmethod
    def save_new_credential(self):
        Credential.credential_list.append(self)
    
  
        
        
        
        
    