from src.services.astralObjectsAdapter import AstralObjectsAdapter


class AstralObject():

    def getRow(self):
        raise NotImplementedError()

    def getColumn(self):
        raise NotImplementedError()
    
    def sendToService(self, service: AstralObjectsAdapter):
        raise NotImplementedError()
