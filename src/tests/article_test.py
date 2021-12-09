import unittest
import articles
from app import db

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
        
    def test_hide_article(self):
        articles.add_new_article("Testi", "Minä", "", "www.testi.fi")
        result = db.session.execute("SELECT id FROM article WHERE title = 'Testi'")
        
        #this is the id of the newly added test data
        idno = result.fetchone()[0]
        
        articles.hide(idno)
        result = db.session.execute("SELECT visible FROM article WHERE id = " + str(idno))
        self.assertEqual(result.fetchone()[0], 0)

    def test_article_has_created_at_information(self):
        article_data = articles.get_all()
        self.assertIsNotNone(article_data[0][6])