import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDPaese(self):
        paesi = self._model.getPaesi()
        for paese in paesi:
            self._view._ddGenre.options.append(ft.dropdown.Option(key=paese,text=paese))

        self._view.update_page()
        pass

    def handleCreaGrafo(self, e):
        try:
            paese_input = str(self._view._ddGenre.value)
            self._model.buildGrafo(paese_input)
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato . \n contiene {self._model.getNumNodi()} nodi e {self._model.getNumArchi()} archi"))
            self._view.update_page()
        except ValueError as e:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"errore : {e}"))
            self._view.update_page()

        pass



    def handleCammino(self,e):
        pass