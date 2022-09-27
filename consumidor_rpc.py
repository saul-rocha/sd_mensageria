from random import randint
import Pyro4
from threading import Thread
import time

ns = Pyro4.locateNS()

uri = ns.lookup('obj')
#produtor acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)


def consumidor():
    fila = input("usuario | funcionario | outros: ")

    while True:
        msg = acesso.receber_mensagem(fila)
        print("mensagem recebida: "+msg)
        
        if msg == "Sem mensagens para receber.":
            time.sleep(2)
        
thread_cons = Thread(target=consumidor)#cria a thread
thread_cons.start()
thread_cons.join()
