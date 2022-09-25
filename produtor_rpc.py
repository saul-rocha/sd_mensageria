import Pyro4
import random
from threading import Thread
import time

ns = Pyro4.locateNS()

uri = ns.lookup('obj')

#produtor acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)

print('\nConectado')


lista_msg = ["olá","tudo bem?", "im Groot", "Se você fosse um peixinho eu seria um beija-flor.", "batatinha quando nasce se espalha pelo chão.", "Lord of the rings better than harry potter."]
def criar_mensagem():
    while True:
        lista_dest = [1,2,3]
        id1 = random.randint(0,len(lista_msg)-1)
        print(id1)
        resultado = lista_msg[id1]
        id2 = random.randint(0,2)
        destino = lista_dest[id2]
        #acesso.add_fila(id1,mensagem)
        acesso.Fanout(resultado)
        print(lista_msg[id1])
        time.sleep(2)


criar_mensagem()


"""resultado_broadcast = acesso.Fanout('Quero enviar esta mensagem para todos departamentos')
print(resultado_broadcast)

thread1 = Thread(target=criar_mensagem, args=[acesso])
time.sleep(1)
thread1.start()"""