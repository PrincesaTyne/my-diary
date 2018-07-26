import unittest, requests

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """This method is called first and
         it initializes the data required for each
          test"""
        self.client = app.test_client()

        self.entries = json.dumps({
            [
            {
            "entryId1": "content1"
            },
            {
            "entryId2": "content2"
            },
            {
            "entryId3": "content3"
            }
            ]
    
    def tearDown(self):
        """This method is called last and
        destroys the previously initialised data"""
        
        entries = []
    


    def get_all_entries(self):
        """Tests get_all_entries method"""
        response = requests.get("/api/v1/entries",
                                data=json.dumps(dict(foo='bar')),
                                content_type='application/json')
            
    def get_single_entry(self, entryId):
        """Tests the get_single_entry method"""
        response = requests.get('/api/v1/entries/{}'.format(entryId),
                               content_type='application/json')

    def add_entry(self):
        """Tests the add_entry method"""
        response = requests.post('/api/v1/entries', data=json.dumps(new_entry),
                                content_type='application/json')

    def edit_entry(self):
        """Tests the edit_entry method"""
        response = requests.put('/api/v1/entries/{}'.format(entryId), data=json.dumps(edited_entry),
                                content_type='application/json')
    
    def remove_entry(self):
        """Tests the remove_entry method"""
        response = requests.delete('/api/v1/entries/{}'.format(entryId), data=json.dumps(edit_info),
                                content_type='application/json')
 
if __name__ == '__main__':
    unittest.main()