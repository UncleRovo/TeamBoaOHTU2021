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
        self.assertIsNotNone(article_data[0][8])

    def test_article_has_empty_taglist_if_no_tags_added(self):
        articles.add_new_article("notags", "who", "", "www.vvv.ee")
        result = db.session.execute("SELECT tag FROM article WHERE title='notags'")
        tag = result.fetchone()[0]

        self.assertListEqual(tag, [])

    def test_article_has_list_of_added_tags(self):
        articles.add_new_article("tagsplease", "who", "", "www.vvv.ee", ["tag1","tag2","tag3"])
        result = db.session.execute("SELECT tag FROM article WHERE title='tagsplease'")
        tag = result.fetchone()[0]

        self.assertListEqual(tag, ["tag1", "tag2", "tag3"])
