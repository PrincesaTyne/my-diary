import unittest, requests

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """This method is called first"""
        print("Tests have began")
    
    def tearDown(self):
        """This method is called last"""
        print("Tests are finished")
    


    def get_all_entries(self):
        """Tests get_all_entries method"""
        response = requests.get("/api/v1/entries",
                                content_type='application/json')
        
            
    def get_single_entry(self, entryId):
        """Tests the get_single_entry method"""
        return self.client.get('/api/v1/entries/{}'.format(entryId),
                               content_type='application/json')

    def add_entry(self):
        """Tests the add_entry method"""
        return self.client.post('/api/v1/entries', data=json.dumps(new_entry),
                                content_type='application/json')

    def edit_entry(self):
        """Tests the edit_entry method"""
        return self.client.put('/api/v1/entries/{}'.format(entryId), data=json.dumps(edited_entry),
                                content_type='application/json')
    
    def remove_entry(self):
        """Tests the remove_entry method"""
        return self.client.delete('/api/v1/entries/{}'.format(entryId), data=json.dumps(edit_info),
                                content_type='application/json')
 
if __name__ == '__main__':
    unittest.main()