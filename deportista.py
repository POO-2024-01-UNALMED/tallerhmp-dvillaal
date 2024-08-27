class Deportista():
    def __init__(self, deporte, añosPracticando):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte
    def setDeporte(self, deporte):
        self._deporte = deporte

    def getañosPracticando(self):
        self._añosPracticando
