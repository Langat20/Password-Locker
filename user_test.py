'''
import unittest to create test cases
import User class from user module and Credential class from credentials module  
'''

import unittest
from credentials import Credential
from user import User

class test_user(unittest.TestCase):
    '''
    test class to define test cases for various user class behaviors
    '''
    
    def setUp(self):
        self.new_user=User("Evans", "langat")
        
    def tearDown(self):
        User.user_list=[]
        
    def test_init(self):
        '''
        to test whether the user object is properly initialized
        '''
        self.assertEqual(self.new_user.username, "Evans")
        self.assertEqual(self.new_user.password, "langat")
        
    def test_save_user(self):
        '''
        To test if a user is being added to the user user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
    
    def test_save_multiple_users(self):
        '''
        method to test if you can save more than one user object
        '''
        self.new_user.save_user()
        test_user=User("lyne", "qwerty")
        test_user1=User("kenny", "qwerty")
        
        #save the new test users
        test_user.save_user()
        test_user1.save_user()
        self.assertEqual(len(User.user_list), 3)
        
    def test_find_credential(self):
        self.new_user.save_user()
        test_user=User("lyne", "qwerty")
        test_user.save_user()
        found_credential=User.find_credential("Paypal")
        self.assertEqual(found_credential, False)
        
    def test_log_in(self):
        '''
        to test whether the user can log in their accounts
        '''
        self.new_user.save_user()
        test_user=User("lyne", "qwerty")
        test_user.save_user()
        found_credential=User.log_in("lyne", "qwerty")
        self.assertEqual(found_credential, Credential.credential_list)
        
    