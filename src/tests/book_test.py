import unittest
import books
from app import db

class TestBook(unittest.TestCase):
    def setUp(self):
        pass

    def test_retrieve_right_amount_of_books_from_database(self):
        amount = len(books.get_all())
        self.assertGreaterEqual(amount, 1)

        books.add_new_book("Outlander", "Diana Gabaldon", "0440212561", 1)
        self.assertGreaterEqual(amount + 1, 2)

    def test_retrieve_one_book_with_right_information(self):
        book = books.get_one(1)
        self.assertEqual(book.author, "J.R.R. Tolkien")
        self.assertEqual(book.title, "The Lord of the Rings")

    def test_book_added_to_database(self):
        success = books.add_new_book("Pride and Prejudice", "Jane Austen", "9780141439518", 1)
        self.assertEqual(success, True)

    def test_hide_book(self):
        books.add_new_book("Hobotti", "Vesa Vierikko", "8679697699", 1)
        result = db.session.execute("SELECT id FROM book WHERE title = 'Hobotti'")

        #this is the id of the newly added test data
        idno = result.fetchone()[0]

        books.hide(idno)
        result = db.session.execute("SELECT visible FROM book WHERE id = " + str(idno))
        self.assertEqual(result.fetchone()[0], 0)

    def test_book_has_created_at_information(self):
        book_data = books.get_all()
        self.assertIsNotNone(book_data[0][7])

    def test_book_has_empty_taglist_if_no_tags_added(self):
        books.add_new_book("notags", "who", "ISBN", 1)
        result = db.session.execute("SELECT tag FROM book WHERE title='notags'")
        tag = result.fetchone()[0]

        self.assertListEqual(tag, [])

    def test_book_has_list_of_added_tags(self):
        books.add_new_book("tagsplease", "who", "ISBN", 1, ["tag1","tag2","tag3"])
        result = db.session.execute("SELECT tag FROM book WHERE title='tagsplease'")
        tag = result.fetchone()[0]

        self.assertListEqual(tag, ["tag1", "tag2", "tag3"])

    def test_get_book_by_user(self):
        result = books.get_by_user(1)

        passTest = True

        #at the moment the 'owner' column is found at index 5. May be subject to change
        for book in result:
            if book[5] != 1:
                passTest = False
                break
        self.assertEqual(passTest, True)

    def test_search_book_by_word_returns_right_information(self):
        searched_books = books.search("lord", 1)
        self.assertEqual(searched_books[0].author, "J.R.R. Tolkien")

    def test_update_book(self):
        books.add_new_book("testikirja", "Teppo Testaaja", "12345", 1, [])
        sql = "SELECT id FROM book WHERE author='Teppo Testaaja'"
        result = db.session.execute(sql)
        id = result.fetchone().id
        attributes = {"title": "testikirja",
                      "author": "Terhi Testaaja",
                      "isbn": "12345",
                      "tag": ""}
        books.update(id, attributes)

        book = books.get_one(id)
        self.assertEqual(book.author, "Terhi Testaaja")

    def test_update_book_with_no_attributes(self):
        success = books.update(1, None)
        self.assertFalse(success)

    def test_update_book_with_invalid_attributes(self):
        success = books.update(1, {"author": "Terhi Testaaja",
                                   "channel": "Terhin testikanava"})
        self.assertFalse(success)