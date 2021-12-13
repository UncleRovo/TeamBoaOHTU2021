import unittest
import blogs
from app import db

class TestArticle(unittest.TestCase):
    def setUp(self):
        pass

    def test_blog_added_to_database(self):
        success = blogs.add_new_blog("ABC", "Virtanen", "www.abc.fi", 1)
        self.assertEqual(success, True)

    def test_retrieve_one_blog_with_right_information(self):
        blog = blogs.get_one(1)
        self.assertEqual(blog.author, "blogger")
        self.assertEqual(blog.title, "Building blogs")

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

    def test_get_blog_by_user(self):
        result = blogs.get_by_user(1)

        passTest = True

        #at the moment the 'owner' column is found at index 5. May be subject to change
        for blog in result:
            if blog[5] != 1:
                passTest = False
                break
        self.assertEqual(passTest, True)

    def test_search_blog_by_word_returns_right_information(self):
        searched_blogs = blogs.search("build", 1)
        self.assertEqual(searched_blogs[0].author, "blogger")

    def test_update_blog(self):
        blogs.add_new_blog("testiblogi", "Teppo Testaaja", "www.testi.fi", 1, [])
        sql = "SELECT id FROM blog WHERE author='Teppo Testaaja'"
        result = db.session.execute(sql)
        id = result.fetchone().id
        attributes = {"title": "testiblogi",
                      "author": "Terhi Testaaja",
                      "url": "www.testi.fi",
                      "tag": ""}
        blogs.update(id, attributes)

        blog = blogs.get_one(id)
        self.assertEqual(blog.author, "Terhi Testaaja")

    def test_update_blog_with_no_attributes(self):
        success = blogs.update(1, None)
        self.assertFalse(success)

    def test_update_blog_with_invalid_attributes(self):
        success = blogs.update(1, {"author": "Terhi Testaaja",
                                   "isbn": 12345})
        self.assertFalse(success)