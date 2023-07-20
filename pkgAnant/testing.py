import unittest 
from passwd import gen_pass

class TestPasswordTester(unittest.TestCase):

    def test_generated_password(self):
        # Generate a password using the gen_pass function
        generated_password = gen_pass()

        # Ensure that the generated password is between 6 and 12 characters
        self.assertTrue(6 <= len(generated_password) <= 12)

        # Ensure that the generated password contains at least one lowercase letter
        self.assertTrue(any(char.islower() for char in generated_password))

        # Ensure that the generated password contains at least one uppercase letter
        self.assertTrue(any(char.isupper() for char in generated_password))

        # Ensure that the generated password contains at least one number
        self.assertTrue(any(char.isdigit() for char in generated_password))

if __name__ == "__main__":
    unittest.main()

