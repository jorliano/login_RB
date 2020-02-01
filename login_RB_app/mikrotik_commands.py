from login_RB_app.servidor import Servidor

class MikrotikComandos:

    list =[]

    def printMK(self,Mikrotik):
        for mk in Mikrotik:
            print(mk.ip+'\n')
            print(mk.login+'\n')
            print(mk.password+'\n')

    def add_logins(self,Mikrotik,data):
        print(data)
        for mk in Mikrotik:
             try:
                 servidor = Servidor(mk)
                 msg = servidor.add_user(data)

                 if len(msg) < 10:
                    self.list.append({'name':mk.name,'tipo':25,'msg':'comando realizado com sucesso'})
                 else:
                    self.list.append({'name':mk.name,'tipo':30,'msg':msg})

             except Exception as e:
                 self.list.append({'name':mk.name,'tipo':40,'msg':'comando falhou'})

        return self.list

    def remover_users(self,Mikrotik,data):
        print(data['name'])
        for mk in Mikrotik:
             try:
                 servidor = Servidor(mk)
                 msg = servidor.remove_user(data['name'])

                 if msg == None:
                    self.list.append({'name':mk.name,'tipo':25,'msg':'comando realizado com sucesso'})
                 else:
                    self.list.append({'name':mk.name,'tipo':30,'msg':msg})

             except Exception as e:
                 self.list.append({'name':mk.name,'tipo':40,'msg':'comando falhou'})
                 print(e)

        return self.list
    def update_user(self,Mikrotik,data):
        print(data)
        for mk in Mikrotik:
             try:
                 servidor = Servidor(mk)
                 msg = servidor.update_user(data)

                 if len(msg) < 10:
                    self.list.append({'name':mk.name,'tipo':25,'msg':'comando realizado com sucesso'})
                 else:
                    self.list.append({'name':mk.name,'tipo':30,'msg':msg})

             except Exception as e:
                 self.list.append({'name':mk.name,'tipo':40,'msg':'comando falhou'})

        return self.list
