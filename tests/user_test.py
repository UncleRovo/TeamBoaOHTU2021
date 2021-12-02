import unittest
import user



class TestUser(unittest.TestCase):
    def setUp(self):
        pass


    def test_add_user_to_the_database(self):
        query = user.register('testi_tepponen', "1234qwerty")
        self.assertEqual(query, True)
