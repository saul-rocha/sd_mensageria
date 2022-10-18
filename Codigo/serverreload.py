import Pyro4
import random
from threading import Thread
import time

ns = Pyro4.locateNS()

uri = ns.lookup('obj')

#produtor acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)


def status():
    print("Atualizando dados, execute o servidor HTTP para visualisálos!")
    while True:
        #op = input("\n-t (tamanho das filas)\n-f (filas criadas)\n-c (consumidores)\n-p (consumidores)\n")
        stt = acesso.status()
        #print(stt)
        text = '''
                <!DOCTYPE html>
                <html>
                    <head>
                        <meta charset="utf-8">
                        <meta http-equiv="refresh" content="10">
                    </head>
                    <body>
                        <h1> Informações <h1>
                        <h2>'''+stt+'''</h2>
                    </body>
                </html>
        '''
        file = open("index.html","w")
        file.write(text)
        file.close()
        time.sleep(5)

import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print("Seu IP local é: ",local_ip)

thread_prod = Thread(target=status)#cria a thread
thread_prod.start()
thread_prod.join()