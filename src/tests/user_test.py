import unittest
import user
import app



class TestUser(unittest.TestCase):
    def setUp(self):
        pass


    def test_add_a_new_user_to_the_database(self):
        query = user.register("testi_tepponen", "1234qwerty")
        self.assertEqual(query, True)

    def test_login_works(self):
        query = user.login("testi_tepponen", "1234qwerty", True)
        self.assertEqual(query, True)
        