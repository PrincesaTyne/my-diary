from flask import Flask
from apis.app import app
import json
import unittest

#app = Flask(__name__)

class TestEntries(unittest.TestCase):
    def setUp(self):
        """ setups any state specific to the execution of
         the given module."""
        self.client = app.test_client(self)

    def tearDown(self):
        """ teardowns any state that was previously 
        setup with a setup_module
        method.
        """
        print("Tests are done")
    
    def test_get_all_entries(self):
        self.client.post("/api/v1/entries",
                        data = json.dumps({'title':'sd','content':'wert','id':'4','date':'89'}),
                        content_type = 'application/json')
        response = self.client.get('/api/v1/entries')
        #self.assertIn("entries", response.data.decode())
        self.assertEqual(response.status_code, 200)
    
    # def test_get_single_entry(self, entryId):
    #         self.client.post("/api/v1/entries",
    #                 data = json.dumps({'title':'sd','content':'wert','id':'4','date':'89'}),
    #                 content_type = 'application/json')
    #     response = self.client.get("/api/v1/entries/{}".format())
    
    # def test_add_entry(self):
    #     response = self.client.get("/api/v1/entries")
    
    # def test_edit_entry(self):
    #     response = self.client.get("/api/v1/entries/{}".format())

    
    if __name__ == '__main__':
        unittest.main()