import time
from threading import Thread

class Produtor(Thread): #cria um objeto da classe Produtor
    def __init__(self): #contrutor da classe
        print("Produtor Criado!")
        self.mensagens = []
        Thread.__init__(self)#contrutor da superclasse que myWorker herda

    def list_mensagens(self):
        return self.mensagens

    def remover_mensagem(self, mensagem):
        self.mensagens.remove(mensagem)
        print("mensagem criada.")

    def roduzir_mensagem(self, mensagem):
        self.mensagens.append(mensagem)
        print("Mensagem produzida")

    def enviar_mensagem(self):
        pass
