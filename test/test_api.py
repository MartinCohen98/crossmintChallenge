import unittest

import requests

from config.config import CANDIDATE_ID, URL


class ApiTest(unittest.TestCase):

    def test_getMapGoal(self):
        response = requests.get(url=URL + "map/" + CANDIDATE_ID + "/goal")
        self.assertTrue(response.status_code == 200)

    def test_polyanets(self):
        requestBody = {'row': 1, 'column': 1, 'candidateId': CANDIDATE_ID}
        response = requests.post(url=URL+"polyanets/", data=requestBody)
        self.assertTrue(response.status_code == 200)
        response = requests.delete(url=URL+"polyanets/", data=requestBody)
        self.assertTrue(response.status_code == 200)

if __name__ == '__main__':
    unittest.main()