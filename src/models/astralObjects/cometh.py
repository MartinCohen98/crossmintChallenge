from .astralObject import AstralObject
from src.services.astralObjectsAdapter import AstralObjectsAdapter
from exceptions.sendingError import SendingAstralObjectError


class Cometh(AstralObject):

    def __init__(self, row: int, column: int, name: str):

        self.row: int = row
        self.column: int = column
        self.direction: str = name.replace("_COMETH", "").lower()
    
    def sendToService(self, service: AstralObjectsAdapter):
        sent = False

        while not sent:
            try:
                service.sendCometh(self.row, self.column, self.direction)
                sent = True
            except SendingAstralObjectError:
                print("Error sending cometh, trying again.")
