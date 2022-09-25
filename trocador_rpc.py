# Python Remote Objects(Biblioteca python para criação de aplicações que se comuniquem pela rede)
#python -m Pyro4.naming
import Pyro4

# Decorator  que permite com que as classes/metódos abaixo sejam expostos para um acesso remoto.
@Pyro4.expose
class Trocador:
    
    def add_fila(self,id, mensagem):
        if id == 1:
            fila1.append(mensagem)
        elif id == 2 :
            fila1.append(mensagem)
        else:
            fila1.append(mensagem)

        print("mensagem direcinada ao consumer{id}")

    def enviar_mensagem(self, id):
        if id == 1 and  fila1 != []:
            return fila1.pop(0)
        elif id == 2 and fila2 != []:
            return fila2.pop(0)
        elif fila3 != []:
            return fila3.pop(0)
        else:
            return "void"
        
        

    def Fanout(self, mensagem):
        mensagem
        fila1.append(mensagem)
        fila2.append(mensagem)
        fila3.append(mensagem)
        print("mensagem Fanout encaminhada")

    def status(self):
        print("Fila1:{}\nFila2:{}\nFila3:{}\n".format(len(fila1),len(fila2),len(fila3)))


fila1 = []
fila2 = []
fila3 = []


# SERVIDOR instancia OBJETO remoto
objeto = Pyro4.Daemon()

# SERVIDOR registra OBJETO e faz um vinculo dele em uma porta.
vinculo = objeto.register(Trocador)
ns = Pyro4.locateNS()
ns.register('obj',vinculo)


# Vinculo que será usado no programa CLIENTE é apresentado na tela
print('Rodando...')

# OBJETO  espera por clientes que invoquem seus metódos.
objeto.requestLoop()