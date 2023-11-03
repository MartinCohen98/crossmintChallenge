import requests

from config.config import CANDIDATE_ID, URL


class CrossmintChallengeService():
    
    def getSolution(self):
        response = requests.get(url = URL + "map/" + CANDIDATE_ID + "/goal")
        response.raise_for_status()
        return response.json()

    def postPolyanet(self, row, column):
        print(f"Sending polyanet in position {row}, {column}")
        requestBody = {'row': row, 'column': column, 'candidateId': CANDIDATE_ID}
        response = requests.post(url = URL + "polyanets/", data = requestBody)
        response.raise_for_status()

    def deletePolyanet(self, row, column):
        requestBody = {'row': row, 'column': column, 'candidateId': CANDIDATE_ID}
        response = requests.delete(url = URL + "polyanets/", data = requestBody)
        response.raise_for_status()
