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

x = SingletonA()
x.setAccion("Camina")
print(x.getAccion())
z = SingletonA()
print(z.getAccion())
y = SingletonB()
y.setAccion("Salta")
print(y.getAccion())
w = SingletonB()
print(w.getAccion())
