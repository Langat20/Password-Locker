import unittest
from credentials import Credential
from user import User

class TestCredentials(unittest.TestCase):
    def setUp(self):
        
        #create a credential object test 
        self.new_credential = Credential("Evans","langat", "twitter", "Uy67tye")
       
    def tearDown(self):
        Credential.credential_list=[]
        
    def test_init(self):
        '''
        Testcase to test of the credential object is properly initialized 
        '''
        self.assertEqual(self.new_credential.user_name, "Evans")
        self.assertEqual(self.new_credential.user_password, "langat")
        self.assertEqual(self.new_credential.credential_name, "twitter")
        self.assertEqual(self.new_credential.credential_password, "Uy67tye")
        
    def test_save_credentials(self):
        '''
        Test case to test if the credential object is saved into the credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)
        
    def test_save_multiple_credentials(self):
        '''
        To test if it is possible to save multiple credentials in the credential list
        '''
        self.new_credential.save_credential()
        test_credential=Credential("Evans", "langat", "gmail", "Wr673fts")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)
        
    def test_generate_passwords(self):
        '''
        To test of the generated password is valid to log into user credentials 
        '''
        test_generated_password=self.new_credential.generate_password()
        self.assertEqual(len(test_generated_password), 6)
        
    def test_display_credentials(self):
        
        #save the new credantial created 
        self.new_credential.save_credential()
        test_credential=Credential("Evans", "langat", "gmail", "Wr673fts")
        test_credential.save_credential()
        new_credential = Credential("Evans", "langat", "twitter", "Uy67tye")
        new_credential.save_credential()
        self.assertEqual(len(Credential.display_credentials("langat")), 3)
        
        
   
        
if __name__ == "__main__":
    unittest.main()
        
        
        
        
        
        