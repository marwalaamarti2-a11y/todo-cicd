class GestionnaireTaches:
    def __init__(self):
        self.taches = []

    def ajouter(self, titre):
        if not titre or not titre.strip():
            raise ValueError("Le titre ne peut pas être vide")
        self.taches.append({"titre": titre.strip(), "terminee": False})

    def supprimer(self, numero):
        self._verifier(numero)
        self.taches.pop(numero - 1)

    def terminer(self, numero):
        self._verifier(numero)
        self.taches[numero - 1]["terminee"] = True

    def lister(self):
        return list(self.taches)

    def _verifier(self, numero):
        if numero < 1 or numero > len(self.taches):
            raise IndexError("Numéro de tâche inexistant")
