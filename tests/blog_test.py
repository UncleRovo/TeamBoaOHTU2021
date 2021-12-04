import unittest
import blogs
from app import db

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
        
    def test_hide_blog(self):
        blogs.add_new_blog("Miten testata", "Kaikki", "www.testi2.fi")
        result = db.session.execute("SELECT id FROM blog WHERE title = 'Miten testata'")
        
        #this is the id of the newly added test data
        idno = result.fetchone()[0]
        
        blogs.hide(idno)
        result = db.session.execute("SELECT visible FROM blog WHERE id = " + str(idno))
        self.assertEqual(result.fetchone()[0], 0)
