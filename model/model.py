import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._idMap={}
        self._best_path=[]
        self._best_weight=-30894807230873208342089342803492
        pass


    def getPaesi(self):
        return DAO.getPaesi()

    def getNodi(self,paese):
        return DAO.getNodi(paese)

    def getNumNodi(self):
        return len(self._grafo.nodes())

    def getNumArchi(self):
        return len(self._grafo.edges())

    def buildGrafo(self,paese):
        self._grafo.clear()
        for nodo in self.getNodi(paese):
            self._grafo.add_node(nodo)


