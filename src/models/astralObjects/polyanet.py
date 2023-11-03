from .astralObject import AstralObject
from src.services.astralObjectsAdapter import AstralObjectsAdapter
from exceptions.sendingError import SendingAstralObjectError


class Polyanet(AstralObject):

    def __init__(self, row: int, column: int):

        self.row: int = row
        self.column: int = column
    
    def sendToService(self, service: AstralObjectsAdapter):
        sent = False

        while not sent:
            try:
                service.sendPolyanet(self.row, self.column)
                sent = True
            except SendingAstralObjectError:
                print("Error sending polyanet, trying again.")
                # Should probably add a sleep timer in case of too many requests
        