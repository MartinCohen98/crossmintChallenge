
from src.models.polyanet import Polyanet
from src.services.crossmintChallengeService import CrossmintChallengeService

class Map():

    def __init__(self, json):

        self.polyanets = []

        grid = json["goal"]

        rowNumber = 0
        columnNumber = 0

        for row in grid:
            for column in row:
                
                if column == "POLYANET":
                    self.polyanets.append(Polyanet(rowNumber, columnNumber))

                columnNumber = columnNumber + 1
            columnNumber = 0
            rowNumber = rowNumber + 1

    def sendPolyanets(self):

        service = CrossmintChallengeService()

        for polyanet in self.polyanets:
            service.postPolyanet(polyanet.getRow(), polyanet.getColumn())