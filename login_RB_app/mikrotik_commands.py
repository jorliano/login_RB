from login_RB_app.servidor import Servidor

class MikrotikComandos:

    def printMK(self,Mikrotik):
        for mk in Mikrotik:
            print(mk.ip+'\n')
            print(mk.login+'\n')
            print(mk.senha+'\n')

    def add_logins(self,Mikrotik,data):
        list =[]
        for mk in Mikrotik:
             try:
                 servidor = Servidor(mk)
                 msg = servidor.add_user(data)

                 if len(msg) < 10:
                    list.append({'descricao':mk.descricao,'tipo':'success','msg':'comando realizado com sucesso'})
                 else:
                    list.append({'descricao':mk.descricao,'tipo':'warning','msg':msg})

             except Exception as e:
                 list.append({'descricao':mk.descricao,'tipo':'danger','msg':'comando falhou'})

        return list

    def remover_users(self,Mikrotik,data):
        list =[]
        for mk in Mikrotik:
             try:
                 print (mk.descricao)
                 servidor = Servidor(mk)
                 msg = servidor.remove_user(data['username'])
                 print('times')

                 if msg == None:
                    list.append({'descricao':mk.descricao,'tipo':'success','msg':'comando realizado com sucesso'})
                 else:
                    list.append({'descricao':mk.descricao,'tipo':'warning','msg':msg})

             except Exception as e:
                 list.append({'descricao':mk.descricao,'tipo':'danger','msg':'comando falhou'})
                 print(e)
        return list
    def update_user(self,Mikrotik,data):
        list =[]
        for mk in Mikrotik:
             try:
                 servidor = Servidor(mk)
                 msg = servidor.update_user(data)

                 if msg == None:
                    list.append({'descricao':mk.descricao,'tipo':'success','msg':'comando realizado com sucesso'})
                 else:
                    list.append({'descricao':mk.descricao,'tipo':'warning','msg':msg})

             except Exception as e:
                 list.append({'descricao':mk.descricao,'tipo':'danger','msg':'comando falhou'})
        return list
