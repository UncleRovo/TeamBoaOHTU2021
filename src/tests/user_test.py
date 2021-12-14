import unittest
import user


class TestUser(unittest.TestCase):
    def setUp(self):
        pass

    def test_new_user_register_will_succeed(self):
        query = user.register("testi_tepponen", "1234qwerty")
        self.assertEqual(query, True)

    # def test_new_user_register_without_password_will_fail(self):
    #     query = user.register("testi_tepponen", '')
    #     self.assertEqual(query, False)

    def test_login_works(self):
        query = user.login("testi_tepponen", "1234qwerty", True)
        self.assertEqual(query, True)

    def test_isLoggedIn_without_login(self):
        logged = user.isLoggedIn()
        self.assertEqual(logged, False)
