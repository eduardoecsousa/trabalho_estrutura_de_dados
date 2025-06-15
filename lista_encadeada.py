class cartao:
    def __init__(self, cor, numero):
        self.cor = cor
        self.numero = numero
        self.proximo = None

    def __repr__(self):
        return self.dado


class lista_encadeada:
    def __init__(self, nodos=None):
        self.head = None
        if nodos is not None:
            elem0 = nodos.pop(0)
            nodo = cartao(cor=elem0[0], numero=elem0[1])
            self.head = nodo
            for elem in nodos:
                nodo.proximo = cartao(cor=elem[0], numero=elem[1])
                nodo = nodo.proximo

    def __repr__(self):
        nodo = self.head
        nodos = []

        while nodo is not None:
            nodos.append(str([nodo.cor, nodo.numero]))
            nodo = nodo.proximo
        return ", ".join(nodos)

    def adicionar_paciente_fila(self, cor, numero):




lista_simples = lista_encadeada([["A", 201], ["A", 202], ["V", 1]])

print(lista_simples.__repr__())