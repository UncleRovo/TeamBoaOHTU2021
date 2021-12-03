import unittest
import blogs

class TestArticle(unittest.TestCase):
    def setUp(self):
        pass

    def test_blog_added_to_database(self):
        success = blogs.add_new_blog("ABC", "Virtanen", "www.abc.fi")
        self.assertEqual(success, True)

    def test_all_blogs_fetched_from_database(self):
        amount = len(blogs.get_all())
        self.assertGreaterEqual(amount, 1)

        blogs.add_new_blog("Best chocolate cake recipe", "mummi", "https://www.google.com")
        self.assertEqual(len(blogs.get_all()), amount + 1)
