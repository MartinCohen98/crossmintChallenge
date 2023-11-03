import requests
from requests import HTTPError

from config.config import CANDIDATE_ID, URL
from exceptions.sendingError import SendingAstralObjectError
from .astralObjectsAdapter import AstralObjectsAdapter


class CrossmintChallengeService(AstralObjectsAdapter):

    def getSolution(self):
        response = requests.get(url = URL + "map/" + CANDIDATE_ID + "/goal")
        response.raise_for_status()
        return response.json()


    def sendPolyanet(self, row: int, column: int):
        try:
            print(f"Sending polyanet in position {row}, {column}")
            requestBody = {'row': row, 'column': column, 'candidateId': CANDIDATE_ID}
            response = requests.post(url = URL + "polyanets/", data = requestBody)
            response.raise_for_status()
        except HTTPError:
            raise SendingAstralObjectError

    def deletePolyanet(self, row: int, column: int):
        requestBody = {'row': row, 'column': column, 'candidateId': CANDIDATE_ID}
        response = requests.delete(url = URL + "polyanets/", data = requestBody)
        response.raise_for_status()

    def sendSoloon(self, row: int, column: int, color: str):
        try:
            print(f"Sending {color} soloon in position {row}, {column}")
            requestBody = {'row': row, 'column': column, 'color': color, 'candidateId': CANDIDATE_ID}
            response = requests.post(url = URL + "soloons/", data = requestBody)
            response.raise_for_status()
        except HTTPError:
            raise SendingAstralObjectError

    def deleteSoloon(self, row: int, column: int, color: str):
        requestBody = {'row': row, 'column': column, 'color': color, 'candidateId': CANDIDATE_ID}
        response = requests.delete(url = URL + "soloons/", data = requestBody)
        response.raise_for_status()

    def sendCometh(self, row: int, column: int, direction: str):
        try:
            print(f"Sending cometh facing {direction} in position {row}, {column}")
            requestBody = {'row': row, 'column': column, 'direction': direction, 'candidateId': CANDIDATE_ID}
            response = requests.post(url = URL + "comeths/", data = requestBody)
            response.raise_for_status()
        except HTTPError:
            raise SendingAstralObjectError

    def deleteCometh(self, row: int, column: int, direction: int):
        requestBody = {'row': row, 'column': column, 'direction': direction, 'candidateId': CANDIDATE_ID}
        response = requests.delete(url = URL + "comeths/", data = requestBody)
        response.raise_for_status()
