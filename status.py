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
        print('\nCalculando...')
        stt = acesso.status()
        print(stt)
        time.sleep(5)
    
thread_prod = Thread(target=status)#cria a thread
thread_prod.start()
thread_prod.join()