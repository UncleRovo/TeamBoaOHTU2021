import unittest
import blogs
from app import db

class TestArticle(unittest.TestCase):
    def setUp(self):
        pass

    def test_blog_added_to_database(self):
        success = blogs.add_new_blog("ABC", "Virtanen", "www.abc.fi", 1)
        self.assertEqual(success, True)

    def test_all_blogs_fetched_from_database(self):
        amount = len(blogs.get_all())
        self.assertGreaterEqual(amount, 1)

        blogs.add_new_blog("Best chocolate cake recipe", "mummi", "https://www.google.com", 1)
        self.assertEqual(len(blogs.get_all()), amount + 1)
        
    def test_hide_blog(self):
        blogs.add_new_blog("Miten testata", "Kaikki", "www.testi2.fi", 1)
        result = db.session.execute("SELECT id FROM blog WHERE title = 'Miten testata'")
        
        #this is the id of the newly added test data
        idno = result.fetchone()[0]
        
        blogs.hide(idno)
        result = db.session.execute("SELECT visible FROM blog WHERE id = " + str(idno))
        self.assertEqual(result.fetchone()[0], 0)

    def test_blog_has_created_at_information(self):
        blog_data = blogs.get_all()
        self.assertIsNotNone(blog_data[0][7])

    def test_blog_has_empty_taglist_if_no_tags_added(self):
        blogs.add_new_blog("notags", "who", "www.vvv.ee", 1)
        result = db.session.execute("SELECT tag FROM blog WHERE title='notags'")
        tag = result.fetchone()[0]

        self.assertListEqual(tag, [])

    def test_blog_has_list_of_added_tags(self):
        blogs.add_new_blog("tagsplease", "who", "www.vvv.ee", 1, ["tag1","tag2","tag3"])
        result = db.session.execute("SELECT tag FROM blog WHERE title='tagsplease'")
        tag = result.fetchone()[0]

        self.assertListEqual(tag, ["tag1", "tag2", "tag3"])