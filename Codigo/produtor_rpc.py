from ast import arg
import Pyro4
import random
from threading import Thread
import time
from optparse import OptionParser

lista_msg = ["olá","tudo bem?", "Muita pressão.", "im Groot.", "Se você fosse um peixinho eu seria um beija-flor.", "batatinha quando nasce se espalha pelo chão.", "Lord of the rings better than harry potter."]
lista_dest = ["usuario", "funcionario","outros","fanout"]


def criar_mensagem(topico,msg_sec):

   while(True):
            
        #dest = input("Qual o destino das mensagem? |cliente | funcionario | outros | fanout")
        #qtd = int(input("Quantidade de mensagens?"))
        #qtd = random.randint(0, 10)
        #for i in range(qtd):
        id1 = random.randint(0,len(lista_msg)-1)
        mensagem = lista_msg[id1]
        if topico == "fanout":
            acesso.send_mensagem("fanout", "ESSE É UM FANOUT")
            print("Fanout enviado!")
        else:
            acesso.send_mensagem(topico, mensagem)
            print("{} enviada para {}".format(mensagem,topico))
        time.sleep(float(msg_sec))
        



if __name__ == "__main__":
    try:
        #parser = OptionParser()
        #parser.add_option("-t", "--topico", dest="topico", default="vazio", help="topico do produtor")
        #parser.add_option("-m", "--mensagem", dest="mensagem", default="vazio", help="Mensagem por segundo")

        #options, args = parser.parse_args()
        ns = Pyro4.locateNS()

        uri = ns.lookup('obj')

        #produtor acessa remotamente SERVIDOR
        acesso = Pyro4.Proxy(uri)

        print('\nConectado')
        
        topico=input("Insira o tópico do produtor: ")
        if(topico=="fanout"):
            pass   
        else:
            acesso.add_produtor(topico)
        msg=float(input("Tempo em segundos para envio de cada mensagem: "))
        #criar_mensagem(options.topico,options.mensagem)
        thread_prod = Thread(target=criar_mensagem,args=(topico,msg), daemon=True)#cria a thread
        thread_prod.start()
        thread_prod.join()
    
    except (KeyboardInterrupt):
        acesso.prodDesconecta(topico)

"""resultado_broadcast = acesso.Fanout('Quero enviar esta mensagem para todos departamentos')
print(resultado_broadcast)

thread1 = Thread(target=criar_mensagem, args=[acesso])
time.sleep(1)
thread1.start()"""