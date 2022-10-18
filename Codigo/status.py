import Pyro4
import random
from threading import Thread
import time
from optparse import OptionParser

ns = Pyro4.locateNS()

uri = ns.lookup('obj')



#produtor acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)
def status():
    global options
    if (options.produtor):
        print(acesso.statusop("produtor"))
    if (options.consumidor):
        print(acesso.statusop("consumidor"))
    if (options.fila):
        aux=acesso.statusop("fila")
        if (aux==False):
            print("Sem filas até o momento!")
        else:
            print("Filas:", *acesso.statusop("fila"))
    if (options.tamanho):
        print(acesso.statusop1('t',options.fila_name))
    if (options.estatistica):
        print(acesso.statusop1('s',options.fila_name))

parser = OptionParser()
parser.add_option("-p", "--produtor", action="store_true", dest="produtor", default=False, help="Produtores Conectados")
parser.add_option("-c", "--consumidor", action="store_true", dest="consumidor", default=False, help="Consumidores Conectados")
parser.add_option("-f", "--filas", action="store_true", dest="fila", default=False, help="Filas Criadas")
parser.add_option("-F", "--Filas", dest="fila_name", default=False, help="Filas Criadas")
parser.add_option("-t", "--tamanho", action="store_true", dest="tamanho", default=False, help="Tamanho da Fila")
parser.add_option("-s", "--estatistica", action="store_true", dest="estatistica", default=False, help="Estatística da Fila")




options, args = parser.parse_args()

thread_prod = Thread(target=status)#cria a thread
thread_prod.start()
thread_prod.join()