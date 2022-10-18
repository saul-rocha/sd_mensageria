from random import randint
import Pyro4
from threading import Thread
import time

ns = Pyro4.locateNS()

uri = ns.lookup('obj')
#produtor acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)
fila=None
contador=0

def consumidor():
    global contador
    global fila
    topics = []
    topicos=acesso.topicos()
    if(topicos == 0):
        pass
    else:
        for x in range(0,len(topicos)):
            topics.append(topicos[x][0])
    print("Tópicos disponíveis: ", *topics)
    fila = input("Digite o topico desejado: ")
    acesso.add_consumidor(fila)
    

    while True:
        msg = acesso.receive_mensagem(fila,contador)
        #print(msg)
        if msg == False:
            #time.sleep(1)
            pass
        else:
            contador+=1
            print("mensagem recebida: "+msg)
        
try:
    consumidor()        
except (KeyboardInterrupt):
    acesso.subDesconecta(fila)        
