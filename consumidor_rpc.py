from random import randint
import Pyro4
import time

ns = Pyro4.locateNS()

uri = ns.lookup('obj')

#produtor acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)

id = int(input("Id(1,2 ou 3): "))
#def receber_mensagem():
while True:
    id = randint(1,4)
    msg = acesso.enviar_mensagem(id)
    print(msg)
    if msg == "void":
        time.sleep(3)
        
