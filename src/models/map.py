from typing import List

from src.models.astralObjects.astralObject import AstralObject
from src.models.astralObjects.cometh import Cometh
from src.models.astralObjects.polyanet import Polyanet
from src.models.astralObjects.soloon import Soloon
from src.services.astralObjectsAdapter import AstralObjectsAdapter


class Map():

    def __init__(self, crossmintService: AstralObjectsAdapter):

        self.service: AstralObjectsAdapter = crossmintService

        self.astralObjects: List[AstralObject] = []

        json = self.service.getSolution()
        grid = json["goal"]

        rowNumber = 0
        columnNumber = 0

        for row in grid:
            for space in row:
                
                if "POLYANET" in space:
                    self.astralObjects.append(Polyanet(rowNumber, columnNumber))
                elif "SOLOON" in space:
                    self.astralObjects.append(Soloon(rowNumber, columnNumber, space))
                elif "COMETH" in space:
                    self.astralObjects.append(Cometh(rowNumber, columnNumber, space))

                columnNumber = columnNumber + 1
            columnNumber = 0
            rowNumber = rowNumber + 1

    def sendAstralObjects(self):

        for astralObject in self.astralObjects:
            astralObject.sendToService(self.service)