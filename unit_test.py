import unittest
import requests



class TestStringMethods(unittest.TestCase):

    def test(self):
        data = {
            "name": "ali",
            "phoneNumber" : "5646",
            "pinCode": 500023
        }
        data = requests.post("http://localhost:5000/registerUser", data)
        self.assertEquals(data.get("phoneNumber") == "5646")
        self.assertNotIn(data.get("name") == "")


if __name__=="main":
    unittest.main




