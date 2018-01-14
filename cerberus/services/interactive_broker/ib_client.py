from ib.ext.EClientSocket import EClientSocket

class IBClient(EClientSocket):
    def __init__(self, wrapper):
        EClientSocket.__init__(self, wrapper)

    def run_interface(self):
        pass
