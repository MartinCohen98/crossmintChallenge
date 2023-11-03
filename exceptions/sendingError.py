class SendingAstralObjectError(Exception):
    """Made to abstract the error from the http implementation,
    should do this for get and delete in a real project
    """

    def __init__(self):
        pass