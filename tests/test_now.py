from flask import Flask
from apis.app import app
from apis.app import entries
import json
import unittest


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
    """ Tests the different endpoints in app.py """
    def setUp(self):
        """ Runs prior to each test and setups any state specific to
         the execution of the given module. """
        self.client = app.test_client(self)

    def tearDown(self):
        """ Runs after each test and teardowns any state that was 
        previously setup with a setup module
        method.
        """
        entries[:] = []
        print("Tests are done")
    
    def test_get_empty_entry(self):
        """ Tests get_all_eentries when entries list is empty. """        
        response = self.client.get('/api/v1/entries')
        print (response)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"There are no entries yet", response.data)
    
    def test_get_all_entries(self):
        """ Tests for success returning all entries. """
        self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        response = self.client.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)
    
    def test_get_single_empty_entry(self):
        """ Tests get_single_entry when entries list is empty. """
        response = self.client.get('/api/v1/entries/4')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"There are no entries yet", response.data)
    
    def test_get_single_entry(self):
        """  Tests for get_single_entry success. """
        self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = "application/json")
        response = self.client.get("/api/v1/entries/4")
        self.assertEqual(response.status_code, 200)
    
    def test_add_entry_valid_inputs(self):
        """ Tests add_entry when key inputs are invalid. """
        self.client.post("/api/v1/entries",
                        data = json.dumps(invalid_entry),
                        content_type = 'application/json')
        response = self.client.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"There are no entries yet",response.data)
    
    def test_add_entry_id_exists(self):
        """ Tests add_entry when id already exists. """
        self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        response=self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"That id is already taken",response.data)
    
    def test_add_entry_null_entry(self):
        """ Tests add_entry when values added are null. """
        response = self.client.post("/api/v1/entries",
                        data = json.dumps(null_entry),
                        content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"One of the fields is empty",response.data)

    def test_add_entry_success(self):
        """ Tests add_entry success. """
        response = self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'went to work yesterday',response.data)
    
    def test_edit_empty_entry(self):
        """ Tests edit_entry when entries list is empty. """
        response = self.client.put('/api/v1/entries/4')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"There are no entries in your diary", response.data)

    def test_edit_entry(self):
        """ Tests edit_entry success. """
        self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        response = self.client.put("/api/v1/entries/4",
                                    data = json.dumps(edited_data),
                                    content_type = 'application/json')                
        self.assertEqual(response.status_code, 200)

    def test_delete_entry_empty(self):
        """ Tests delete_entry when entries list is empty. """
        response = self.client.delete('/api/v1/entries/4')
        self.assertEqual(response.status_code, 200)
        
    def test_delete_entry(self):
        """  Tests for delete_entry success. """
        self.client.post("/api/v1/entries",
                        data = json.dumps(dummy),
                        content_type = 'application/json')
        response = self.client.delete('/api/v1/entries/4')
        self.assertEqual(response.status_code, 200)

    
    if __name__ == '__main__':
        unittest.main()