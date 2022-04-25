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
        
   