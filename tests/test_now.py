from flask import Flask
from apis.app import app
from apis.app import entries
import json
import unittest



#Dummy data

dummy = {'title':'work',
        'content':'went to work yesterday',
        'id':'4',
        'date':'1/1/2000'}

invalid_entry = {'author':'work',
            'content':'went to work yesterday',
            'id':'4',
            'date':'1/1/2000'}

null_entry = {'title':'',
        'content':'went to work yesterday',
        'id':'4',
        'date':'1/1/2000'}

edited_data = {'title':'work',
            'content':'edited',
            'id':'4',
            'date':'1/1/2000'}

class TestEntries(unittest.TestCase):
    def setUp(self):
        """Runs prior to each test and setups any state specific to
         the execution of the given module."""
        self.client = app.test_client(self)



    def tearDown(self):
        """Runs after each test and teardowns any state that was 
        previously setup with a setup module
        method.
        """
        entries[:] = []
        print("Tests are done")
    
    #Test whether entries is empty
    def test_get_empty_entry(self):
        response = self.client.get('/api/v1/entries')
        print (response)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"There are no entries yet", response.data)
    
    #Test for successfully returning all entries
    def test_get_all_entries(self):
        self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        response = self.client.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)
    
    #Test whether entries is empty
    def test_get_single_empty_entry(self):
        response = self.client.get('/api/v1/entries/4')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"There are no entries yet", response.data)
    
    #Test whther get single entry is a success
    def test_get_single_entry(self):
        self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        response = self.client.get("/api/v1/entries/4")
        self.assertEqual(response.status_code, 200)
    
    #Test edit_entry when entries is empty
    def test_edit_empty_entry(self):
        response = self.client.put('/api/v1/entries/4')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"There are no entries in your diary", response.data)
    
    #Test edit_entry success
    def test_edit_entry(self):
        self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        response = self.client.put('/api/v1/entries/4')
        self.assertEqual(response.status_code, 200)
    
    #Test add_entry check whether key inputs are are valid
    def test_add_entry_valid_inputs(self):
        self.client.post("/api/v1/entries",
                        data = json.dumps(invalid_entry),
                        content_type = 'application/json')
        response = self.client.get('/api/v1/entries')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"There are no entries yet",response.data)
    
        #Test add_entry check whether id already exists
    def test_add_entry_id_exists(self):
        self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        response=self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        # response = self.client.get('/api/v1/entries')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"That id is already taken",response.data)
    
    def test_add_entry_null_entry(self):
        response = self.client.post("/api/v1/entries",
                        data = json.dumps(null_entry),
                        content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"One of the fields is empty",response.data)

    def test_add_entry_success(self):
        response = self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'went to work yesterday',response.data)
    
    def test_edit_entry_valid(self):
        self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        response = self.client.put("/api/v1/entries/4",
                                    data = json.dumps(edited_data),
                                    content_type = 'application/json')                
        self.assertEqual(response.status_code, 200)
        # print(response)
        # self.assertIn(b'went to work yesterday',response.data)

    
    if __name__ == '__main__':
        unittest.main()