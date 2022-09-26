# Python Remote Objects(Biblioteca python para criação de aplicações que se comuniquem pela rede)
#python -m Pyro4.naming
from unicodedata import name
import Pyro4
from threading import Thread
import time

# Decorator  que permite com que as classes/metódos abaixo sejam expostos para um acesso remoto.
@Pyro4.expose
class Trocador():

    """def verifica_consumidor(consumer, receber_mensagem):
        
        for i in range(len(consumidores)):
            if consumidores[i].name == consumer:
                break
        
        thread_consumer =  Thread(target=receber_mensagem)#cria a thread
        thread_consumer.name = name
        consumidores.append(thread_consumer)

        return thread_consumer"""



    def enviar_mensagem(self,id, mensagem):
        if id == "usuario":
            fila1.append(mensagem)
        elif id == "funcionario" :
            fila2.append(mensagem)
        elif id == "outros":
            fila3.append(mensagem)
        else:
            filaFanout.append(mensagem)

        print("mensagem direcinada a {}".format(id))

    def receber_mensagem(self, id):
        if filaFanout != []:
            while (filaFanout != []):
                lista_fan = []
                item = filaFanout.pop(len(filaFanout)-1)
                lista_fan.append(item)
            return lista_fan
    
        elif id == "usuario" and  fila1 != []:
            return fila1.pop(0)
        elif id == "funcionário" and fila2 != []:
            return fila2.pop(0)
        elif id == "outros" and fila3 != []:
            return fila3.pop(0)
        else:
            return "void"
        
        
    def Fanout(self, mensagem):
        filaFanout.append(mensagem)
        print("<mensagem Fanout encaminhada>: {}\n".format(mensagem))

    def status(self):
        return "Fila1:{}\nFila2:{}\nFila3:{}\nPilha de Fanout: {}".format(len(fila1),len(fila2),len(fila3), len(filaFanout))




#Cada fila deve ser mantida por uma Thread.

lista_consumers = ["cliente", "funcionario", "outros"]

filaFanout = []
fila1 = []
fila2 = []
fila3 = []


# SERVIDOR instancia OBJETO remoto
objeto = Pyro4.Daemon()

# SERVIDOR registra OBJETO e faz um vinculo dele em uma porta.
vinculo = objeto.register(Trocador)
ns = Pyro4.locateNS()
ns.register('obj',vinculo)


# Vinculo que será usado no programa CLIENTE é apresentado na tela
print('Rodando...')

# OBJETO  espera por clientes que invoquem seus metódos.
objeto.requestLoop()