from netmiko import Netmiko
from login_RB_app.models import Mikrotik

class MikrotikComandos:

    def printMK(self,Mikrotik):
        for mk in Mikrotik:
            print(mk.ip+'\n')
            print(mk.login+'\n')
            print(mk.password+'\n')


    def add_logins(self,Mikrotik,data):
        for mk in Mikrotik:
             try:
                 #dados da conexao do equipamento
                 plataforma = {
                     "host": mk.ip,
                     "username": mk.login,
                     "password": mk.password,
                     "device_type": "mikrotik_routeros",
                 }

                 net_connect = Netmiko(**plataforma)
                 command = net_connect.send_command("/system")
                 command = net_connect.send_command("/user")
                 command = net_connect.send_command("add name=teste2 password=teste group=read")
                 net_connect.disconnect()
                 print(mk.ip+'\n')
                 print("Comando realizado com sucesso")
                 print(data)
             except Exception as e:
                 print("Ouve um erro :")
                 print(e)
