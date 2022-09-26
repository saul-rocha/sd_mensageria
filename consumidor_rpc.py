from random import randint
import Pyro4
from threading import Thread
import time

ns = Pyro4.locateNS()

uri = ns.lookup('obj')
#produtor acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)

#id = int(input("Id(1,2 ou 3): "))
#def receber_mensagem():

lista_dest = ["cliente", "funcionario","outros"]
def consumidor():
    
    while True:
        id = randint(0,2)

        lista_fan = acesso.receber_mensagem(lista_dest[id])
        if str(type(lista_fan)) == "<class 'list'>" and lista_fan != []:
            for i in lista_fan:
                print("mensagem recebida: "+i)
        else:
            msg = acesso.receber_mensagem(lista_dest[id])
            print("mensagem recebida: "+msg)
            if msg == "void":
                time.sleep(2)
        
thread_cons = Thread(target=consumidor)#cria a thread
thread_cons.start()
thread_cons.join()
