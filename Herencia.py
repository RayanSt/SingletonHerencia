class SingletonAbstract(object):
    _instance = None
    Accion = ""

    def __new__(self):
        if not self._instance:
            self._instance = super(SingletonAbstract, self).__new__(self)
        return self._instance

    def setAccion(self, msg):
        self.Accion = msg

    def getAccion(self):
        return self.Accion


class SingletonA(SingletonAbstract):
    def __init__(self):
        super()


class SingletonB(SingletonAbstract):
    def __init__(self):
        super()

A = SingletonA()
A.setAccion("Camina")
print(A.getAccion())
B = SingletonA()
print(B.getAccion())
C = SingletonB()
C.setAccion("Salta")
print(C.getAccion())
D = SingletonB()
print(D.getAccion())
