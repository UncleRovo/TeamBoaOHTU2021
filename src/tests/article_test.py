import unittest
import articles
from app import db

class TestArticle(unittest.TestCase):
    def setUp(self):
        pass

    def test_article_added_to_database(self):
        success = articles.add_new_article("ABC", "Virtanen", "", "www.abc.fi", 1)
        self.assertEqual(success, True)

    def test_all_articles_fetched_from_database(self):
        amount = len(articles.get_all())
        self.assertGreaterEqual(amount, 2)

        articles.add_new_article("Testing stuff", "T. Esting", "10.9876/54321", "", 1)
        self.assertEqual(len(articles.get_all()), amount + 1)

    def test_retrieve_one_article_with_right_information(self):
        article = articles.get_one(1)
        self.assertEqual(article.author, "James B. Rew")
        self.assertEqual(article.title, "How to brew a cup of coffee")

    def test_hide_article(self):
        articles.add_new_article("Testi", "Minä", "", "www.testi.fi", 1)
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
        articles.add_new_article("notags", "who", "", "www.vvv.ee", 1)
        result = db.session.execute("SELECT tag FROM article WHERE title='notags'")
        tag = result.fetchone()[0]

        self.assertListEqual(tag, [])

    def test_article_has_list_of_added_tags(self):
        articles.add_new_article("tagsplease", "who", "", "www.vvv.ee", 1, ["tag1","tag2","tag3"])
        result = db.session.execute("SELECT tag FROM article WHERE title='tagsplease'")
        tag = result.fetchone()[0]

        self.assertListEqual(tag, ["tag1", "tag2", "tag3"])

    def test_get_article_by_user(self):
        result = articles.get_by_user(1)

        passTest = True

        #at the moment the 'owner' column is found at index 6. May be subject to change
        for article in result:
            if article[6] != 1:
                passTest = False
                break
        self.assertEqual(passTest, True)

    def test_search_article_by_word_returns_right_information(self):
        searched_articles = articles.search("kirjasto", 1)
        self.assertEqual(searched_articles[0].author, "Helsinki")

    def test_update_article(self):
        articles.add_new_article("testiartikkeli", "Teppo Testaaja", "", "www.testi.fi", 1, [])
        sql = "SELECT id FROM article WHERE author='Teppo Testaaja'"
        result = db.session.execute(sql)
        id = result.fetchone().id
        attributes = {"title": "testiartikkeli",
                      "author": "Terhi Testaaja",
                      "resource_id_type": "url",
                      "resource_id": "www.testi.fi",
                      "tag": ""}
        articles.update(id, attributes)

        article = articles.get_one(id)
        self.assertEqual(article.author, "Terhi Testaaja")

    def test_update_article_with_no_attributes(self):
        success = articles.update(1, None)
        self.assertFalse(success)

    def test_update_article_with_invalid_attributes(self):
        success = articles.update(1, {"author": "Terhi Testaaja",
                                      "isbn": 12345})
        self.assertFalse(success)