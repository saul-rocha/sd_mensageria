import Pyro4
import random
from threading import Thread
import time

ns = Pyro4.locateNS()

uri = ns.lookup('obj')

#produtor acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)

print('\nConectado')


lista_msg = ["olá","tudo bem?", "Muita pressão.", "im Groot.", "Se você fosse um peixinho eu seria um beija-flor.", "batatinha quando nasce se espalha pelo chão.", "Lord of the rings better than harry potter."]
lista_dest = ["usuario", "funcionario","outros","fanout"]
def criar_mensagem():

   while(True):
            
        #dest = input("Qual o destino das mensagem? |cliente | funcionario | outros | fanout")
        #qtd = int(input("Quantidade de mensagens?"))
        qtd = random.randint(0, 10)
        for i in range(qtd):
            #quantidade de mensagens
            id = random.randint(0, 3)
            id1 = random.randint(0,len(lista_msg)-1)
            mensagem = lista_msg[id1]
            if lista_dest[id] == "fanout":
                acesso.Fanout(mensagem)
                print("Fanout enviado!")
            else:
                acesso.enviar_mensagem(lista_dest[id], mensagem)
                print("Mensagem para {} enviada!".format(lista_dest[id]))
        time.sleep(2)
        

thread_prod = Thread(target=criar_mensagem)#cria a thread
thread_prod.start()
thread_prod.join()

"""resultado_broadcast = acesso.Fanout('Quero enviar esta mensagem para todos departamentos')
print(resultado_broadcast)

thread1 = Thread(target=criar_mensagem, args=[acesso])
time.sleep(1)
thread1.start()"""