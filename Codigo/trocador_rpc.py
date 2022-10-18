# Python Remote Objects(Biblioteca python para criação de aplicações que se comuniquem pela rede)
#python -m Pyro4.naming
import Pyro4
from threading import Thread
import time
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Decorator  que permite com que as classes/metódos abaixo sejam expostos para um acesso remoto.
@Pyro4.expose
class Trocador():
    

    """def verifica_consumidor(consumer, receber_mensagem):
        
        for i in range(len(consumidores)):
            if consumidores[i].name == consumer:
                break
        
        thread_consumer =  Thread(target=receber_mensagem)#cria a thread
        thread_consumer.name = name
        consumidores.append(thread_consumer)

        return thread_consumer"""

    def add_produtor(self,prod_topico):
        global produtores
        if(len(topicos)==0):
            topicos.append([prod_topico,[]])
            produtores +=1
            print ("Produtor adicionado ao tópico:", prod_topico)
            return True
        for x in topicos:
            if x[0] == prod_topico:
                produtores +=1
                print ("Produtor adicionado ao tópico:", prod_topico)
                return False
        produtores +=1
        topicos.append([prod_topico,[]])
        print ("Produtor adicionado ao tópico:", prod_topico)
        return True

    def add_consumidor(self,topico):
        global consumidores
        print ("Consumidor adicionado ao tópico:", topico)
        consumidores += 1
        return True

    def send_mensagem(self,topico,mensagem):
        global t_mensagem
        for x in range(0,len(topicos)):
            if topicos[x][0] == topico or topico == "fanout":
                #print(topicos[x][0])
                topicos[x][1].append(mensagem)
                t_mensagem+=1
        return False

    def receive_mensagem(self,topico,last):
        global r_mensagem
        for x in range(0,len(topicos)):
            if topicos[x][0] == topico:
                if len(topicos[x][1])==0 or last>=len(topicos[x][1]):
                    #return "SEM MENSAGEM"
                    return False
                r_mensagem+=1
                #print(topicos[x][1][0])
                return topicos[x][1][last]
        return False

    def enviar_mensagem(self,id, mensagem):
        if id == "usuario":
            fila1.append(mensagem)
        elif id == "funcionario" :
            fila2.append(mensagem)
        elif id == "outros":
            fila3.append(mensagem)
        else:
            filaFanout.append(mensagem)

        print("mensagem direcinada a {}".format(id))

    def receber_mensagem(self, id):
        if filaFanout != []:
            item = filaFanout.pop(len(filaFanout)-1)
            return item
        elif id == "usuario" and  fila1 != []:
            return fila1.pop(0)
        elif id == "funcionario" and fila2 != []:
            return fila2.pop(0)
        elif id == "outros" and fila3 != []:
            return fila3.pop(0)
        else:
            return "Sem mensagens para receber."
        
        
    def Fanout(self, mensagem):
        filaFanout.append(mensagem)
        print("<mensagem Fanout encaminhada>: {}\n".format(mensagem))

    def status(self):
        global produtores
        global consumidores
        global t_mensagem
        global r_mensagem
        return " Produtores:{} \n Consumidores:{}\n Mensagens Recebidas:{} \n Mensagens Transmitidas: {}".format(produtores,consumidores,t_mensagem, r_mensagem)

    
    def statusop(self, op):
        global produtores
        global consumidores
        global t_mensagem
        global r_mensagem
        topics=[]
        if op == "produtor":
            return "Produtores:{}".format(produtores)
        if op == "consumidor":
            return "Consumidores:{}".format(consumidores)
        if op == "fila":
            topicos=self.topicos()
            if(topicos == 0):
                return False
            else:
                for x in range(0,len(topicos)):
                    topics.append(topicos[x][0])
            return topics

    def statusop1(self, op, op1):
        global produtores
        global consumidores
        global t_mensagem
        global r_mensagem
        if op == 't':
            mensagens=self.fila_mensagens(op1)
            if mensagens == False:
                return "Sem filas / Fila não encontrada"
            return "{}: {} mensagens".format(op1,mensagens)
        if op == "s":
            mensagens=self.fila_mensagens(op1)
            if mensagens == False:
                return "Sem filas / Estatística de fila não encontrada"
            return "{}: {} mensagens".format(op1,self.fila_mensagens(op1))

    
    def fila_mensagens(self,fila):
        if len(topicos) == 0:
            return False
        for x in topicos:
            if x[0] == fila:
                return len(x[1]) 
        return False


    def topicos(self):
        topics=[]
        if len(topicos) == 0:
            return 0
        for x in topicos:
            topics.append(x)
        return topics
    
    
    def total_topicos(self):
        qtd=0
        if len(topicos) == 0:
            return 0
        for x in topicos:
            qtd+=1
        return qtd
    
    def gerenciar_filas(self):
        pass

    def subDesconecta(self,topico):
        global consumidores
        if topico == None:
            pass
        else:
            print("Consumidor se desconectou do tópico: ", topico)
            consumidores -= 1
    
    def prodDesconecta(self,topico):
        global produtores
        if topico == None:
            pass
        else:
            print("Produtor se desconectou(Tópico: ",topico,")")
            consumidores -= 1

#Cada fila deve ser mantida por uma Thread.

lista_consumers = ["cliente", "funcionario", "outros"]

filaFanout = []
fila1 = []
fila2 = []
fila3 = []

topicos = []
produtores = 0
consumidores = 0
t_mensagem = 0
r_mensagem = 0
# SERVIDOR instancia OBJETO remoto
objeto = Pyro4.Daemon(host=local_ip)



# SERVIDOR registra OBJETO e faz um vinculo dele em uma porta.
vinculo = objeto.register(Trocador)
ns = Pyro4.locateNS()
ns.register('obj',vinculo)


# Vinculo que será usado no programa CLIENTE é apresentado na tela
print('Rodando...')

# OBJETO  espera por clientes que invoquem seus metódos.
objeto.requestLoop()