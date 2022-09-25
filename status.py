import Pyro4
import random
from threading import Thread
import time

ns = Pyro4.locateNS()

uri = ns.lookup('obj')

#produtor acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)

print('\nCalculando...')
while True:
    acesso.status()
    time.sleep(5)
    
