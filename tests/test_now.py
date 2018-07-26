from tests.test_base import BaseTestCase
import pytest
import unittest
from flask import Flask, jsonify, request

app = Flask(__name__)

class TestEntries(BaseTestCase):
    def setUp(self):
        """ setups any state specific to the execution of
         the given module."""
        pass

    def tearDown(self):
        """ teardowns any state that was previously 
        setup with a setup_module
        method.
        """
        pass
    
    def test_get_all_entries(self):
        response = self.client.get("/api/v1/entries")
        self.assertIn("entries", response.data.decode())
        #self.assertEqual(response.status_code, 200) 
        #response = get_all_entries()
        #assert response.status_code == 200
    
    def test_get_single_entry(self, entryId):
        response = self.client.get("/api/v1/entries/{}".format(entryId))
    
    def test_add_entry(self):
        response = self.client.get("/api/v1/entries")
    
    def test_edit_entry(self):
        response = self.client.get("/api/v1/entries/{}".format(entryId))
    
    def test_remove_entry(self):
        response = self.client.get("/api/v1/entries/{}".format(entryId))
    
    if __name__ == '__main__':
        unittest.main()