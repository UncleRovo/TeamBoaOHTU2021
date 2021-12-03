import unittest
import books

class TestBook(unittest.TestCase):
    def setUp(self):
        pass

    def test_retrieve_right_amount_of_books_from_database(self):
        amount = len(books.get_all())
        self.assertGreaterEqual(amount, 1)

        books.add_new_book("Outlander", "Diana Gabaldon", "0440212561")
        self.assertGreaterEqual(amount + 1, 2)


    def test_book_added_to_database(self):
        success = books.add_new_book("Pride and Prejudice", "Jane Austen", "9780141439518")
        self.assertEqual(success, True)