import unittest
import articles

class TestArticle(unittest.TestCase):
    def setUp(self):
        pass

    def test_article_added_to_database(self):
        success = articles.add_new_article("ABC", "Virtanen", "", "www.abc.fi")
        self.assertEqual(success, True)

    def test_all_articles_fetched_from_database(self):
        amount = len(articles.get_all())
        self.assertGreaterEqual(amount, 2)

        articles.add_new_article("Testing stuff", "T. Esting", "10.9876/54321", "")
        self.assertEqual(len(articles.get_all()), amount + 1)
