import unittest
import blogs

class TestArticle(unittest.TestCase):
    def setUp(self):
        pass

    def test_blog_added_to_database(self):
        success = blogs.add_new_blog("ABC", "Virtanen", "www.abc.fi")
        self.assertEqual(success, True)
