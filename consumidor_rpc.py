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
        lista_fan = acesso.receber_mensagem(fila)
        if str(type(lista_fan)) == "<class 'list'>" and lista_fan != []:
            for i in lista_fan:
                print("mensagem recebida: "+i)
        else:
            msg = acesso.receber_mensagem(fila)
            print("mensagem recebida: "+msg)
            if msg == "void":
                time.sleep(2)
        
thread_cons = Thread(target=consumidor)#cria a thread
thread_cons.start()
thread_cons.join()
