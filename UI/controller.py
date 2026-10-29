import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    def mostra_strumenti(self,e):
        lista_strumenti = self._model.get_strumenti()
        self._view.lista_strumenti.controls.clear()
        for strumento in lista_strumenti:
            self._view.lista_strumenti.controls.append(ft.Text(value=f"{strumento['tipo'], strumento['marca'], strumento['anno_acquisto'], strumento['valore'], strumento['disponibile']}"))
        self._view.update()

    def cerca_strumenti(self,e):
        valore = self._view.barra_ricerca.value
        if valore:
            tipo_cercato = valore.strip()
        else:
            tipo_cercato = ""
        self._view.lista_risultati.controls.clear()
        if not tipo_cercato :
            self._view.lista_risultati.controls.append(
                ft.Text("Inserire un tipo di strumento prima di effettuare la ricerca")
            )
            self._view.update()
            return
        risultati = self._model.cerca_strumenti_per_tipo(tipo_cercato)


        if  not risultati:
            self._view.lista_risultati.controls.append(
                ft.Text(f"Nessuno strumento trovato per il tipo: {tipo_cercato}")
            )
        else:
            for strumento in risultati:
                self._view.lista_risultati.controls.append(
                    ft.Text(f"{strumento['marca']} - {strumento['tipo']} - Codice: {strumento['codice']}")
                )
        self._view.update()




