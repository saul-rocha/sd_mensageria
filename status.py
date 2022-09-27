import Pyro4
import random
from threading import Thread
import time

ns = Pyro4.locateNS()

uri = ns.lookup('obj')

#produtor acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)
def status():
    while True:
        op = input("\n-t (tamanho das filas)\n-f (filas criadas)\n-c (consumidores)\n-p (consumidores)\n")
        stt = acesso.status(op)
        print(stt)
    
thread_prod = Thread(target=status)#cria a thread
thread_prod.start()
thread_prod.join()