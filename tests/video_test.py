import unittest
import videos

class TestArticle(unittest.TestCase):
    def setUp(self):
        pass

    def test_retrieve_right_amount_of_videos_from_database(self):
        videos_original = videos.get_all()
        self.assertGreaterEqual(len(videos_original), 2)


    def test_video_added_to_database(self):
        success = videos.add_new_video("ABCvideo", "ABCchannel", "https://www.google.com")
        self.assertEqual(success, True)
    