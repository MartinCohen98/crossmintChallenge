class AstralObjectsAdapter():
    """Not necesary in python, but might be useful in case we need to 
    change services but want to keep using the model
    """

    def getSolution(self):
        raise NotImplementedError()

    def sendPolyanet(self, row: int, column: int):
        raise NotImplementedError()

    def deletePolyanet(self, row: int, column: int):
        raise NotImplementedError()

    def sendSoloon(self, row: int, column: int, color: str):
        raise NotImplementedError()

    def deleteSoloon(self, row: int, column: int, color: str):
        raise NotImplementedError()

    def sendCometh(self, row: int, column: int, direction: str):
        raise NotImplementedError()

    def deleteCometh(self, row: int, column: int, direction: str):
        raise NotImplementedError()
