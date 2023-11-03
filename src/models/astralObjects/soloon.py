from .astralObject import AstralObject
from src.services.astralObjectsAdapter import AstralObjectsAdapter
from exceptions.sendingError import SendingAstralObjectError


class Soloon(AstralObject):

    def __init__(self, row: int, column: int, name: str):

        self.row: int = row
        self.column: int = column
        self.color: str = name.replace("_SOLOON", "").lower()
    
    def sendToService(self, service: AstralObjectsAdapter):
        sent = False

        while not sent:
            try:
                service.sendSoloon(self.row, self.column, self.color)
                sent = True
            except SendingAstralObjectError:
                print("Error sending polyanet, trying again.")
                # Should probably add a sleep timer in case of too many requests