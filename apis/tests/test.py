import requests, json, unittest

response = requests.get("/entries")
print (json.dumps(response.json(), indent=4))

class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(Cls):
        print "runs before setup mthd"
    @classmethod
    def tearDownClass(Cls):
        print "runs after setup mthd"
    
    def setUp(self):
        print "runs at the begining of testing"
    
    def tearDown(self):
        print "runs at the end of testing"

    def test_exercise(self):
        print "i am another test"

    def test_sample(self):
        print "i am a sample test"