import unittest
import articles

class TestArticle(unittest.TestCase):
    def setUp(self):
        pass

    def test_article_added_to_database(self):
        success = articles.add_new_article("ABC", "Virtanen", "", "www.abc.fi")
        self.assertEqual(success, True)
