import unittest
import videos
from app import db

class TestArticle(unittest.TestCase):
    def setUp(self):
        pass

    def test_retrieve_right_amount_of_videos_from_database(self):
        videos_original = videos.get_all()
        self.assertGreaterEqual(len(videos_original), 2)
    
    def test_retrieve_one_video_with_right_information(self):
        video = videos.get_one(1)
        self.assertEqual(video.channel, "Kings and Generals")
        self.assertEqual(video.title, "How Caesar Won the Greast Roman Civil War")

    def test_video_added_to_database(self):
        success = videos.add_new_video("ABCvideo", "ABCchannel", "https://www.google.com", 1)
        self.assertEqual(success, True)

    def test_hide_video(self):
        videos.add_new_video("Titteli", "Kanava", "www.liianpitka.fi/watch/okdeo", 1)
        result = db.session.execute("SELECT id FROM video WHERE title = 'Titteli'")

        #this is the id of the newly added test data
        idno = result.fetchone()[0]

        videos.hide(idno)
        result = db.session.execute("SELECT visible FROM video WHERE id = " + str(idno))
        self.assertEqual(result.fetchone()[0], 0)

    def test_video_has_created_at_information(self):
        video_data = videos.get_all()
        self.assertIsNotNone(video_data[0][7])

    def test_video_has_empty_taglist_if_no_tags_added(self):
        videos.add_new_video("notags", "channel saimaa", "kurl", 1)
        result = db.session.execute("SELECT tag FROM video WHERE title='notags'")
        tag = result.fetchone()[0]

        self.assertListEqual(tag, [])

    def test_video_has_list_of_added_tags(self):
        videos.add_new_video("tagsplease", "channel saimaa", "kurl", 1, ["tag1","tag2","tag3"])
        result = db.session.execute("SELECT tag FROM video WHERE title='tagsplease'")
        tag = result.fetchone()[0]

        self.assertListEqual(tag, ["tag1", "tag2", "tag3"])
        
    def test_get_video_by_user(self):
        result = videos.get_by_user(1)
        
        passTest = True
        
        #at the moment the 'owner' column is found at index 5. May be subject to change
        for video in result:
            if video[5] != 1:
                passTest = False
                break
        self.assertEqual(passTest, True)
    
    def test_search_video_by_word_returns_right_information(self):
        searched_videos = videos.search("cute", 1)
        self.assertEqual(searched_videos[0].channel, "Rufus")

    def test_update_video(self):
        videos.add_new_video("testivideo", "Tepon testikanava", "www.testitube.com", 1, [])
        sql = "SELECT id FROM video WHERE channel='Tepon testikanava'"
        result = db.session.execute(sql)
        id = result.fetchone().id
        attributes = {"title": "testivideo",
                      "channel": "Terhin testikanava",
                      "url": "www.testitube.com",
                      "tag": ""}
        videos.update(id, attributes)

        video = videos.get_one(id)
        self.assertEqual(video.channel, "Terhin testikanava") 