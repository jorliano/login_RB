from librouteros.login import plain, token
from librouteros.query import Key
from librouteros import connect

class Servidor:
    # for post 6.42 (plain text password)
    method = plain
    # for pre 6.43 (with token)
    method = token
    api = ()

    def __init__(self, mk):
            self.api = connect(username=mk.login, password=mk.senha, host=mk.ip, login_method=token)


    def get_user(self,user_name):
        for user in self.api.path("user").select(Key('.id')).where(Key('name') == user_name):
            if user != None and user_name != 'admin':
                return user['.id']
        return False

    def get_all(self):
        tuple(api.path("user"))

    def add_user(self,mikrotik):
        user_id = self.get_user(mikrotik['username'])
        if user_id:
            return 'usuario já exite'
        return self.api.path("user").add(name=mikrotik['username'],password=mikrotik['senha'],group=mikrotik['nivel'])

    def remove_user(self,name):
        user_id = self.get_user(name)
        if user_id:
            return self.api.path("user").remove(user_id)
        return 'falha ao remover usuario'

    def update_user(self,mikrotik):
        user_id = self.get_user(mikrotik['username'])
        if user_id:
            params = {'password':mikrotik['senha'],'group': mikrotik['nivel'], '.id' :user_id}
            return  self.api.path("user").update(**params)
        return 'falha ao atualizar usuario'

    def close(self):
        api.close()
