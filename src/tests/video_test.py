import unittest
import videos
from app import db

class TestArticle(unittest.TestCase):
    def setUp(self):
        pass

    def test_retrieve_right_amount_of_videos_from_database(self):
        videos_original = videos.get_all()
        self.assertGreaterEqual(len(videos_original), 2)


    def test_video_added_to_database(self):
        success = videos.add_new_video("ABCvideo", "ABCchannel", "https://www.google.com")
        self.assertEqual(success, True)
        
    def test_hide_video(self):
        videos.add_new_video("Titteli", "Kanava", "www.liianpitka.fi/watch/okdeo")
        result = db.session.execute("SELECT id FROM video WHERE title = 'Titteli'")
        
        #this is the id of the newly added test data
        idno = result.fetchone()[0]
        
        videos.hide(idno)
        result = db.session.execute("SELECT visible FROM video WHERE id = " + str(idno))
        self.assertEqual(result.fetchone()[0], 0)

    def test_video_has_created_at_information(self):
        video_data = videos.get_all()
        self.assertIsNotNone(video_data[0][6])
    
