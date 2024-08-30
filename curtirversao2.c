class Perfil(object):
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print("nome:%s, telefone:%s, empresa:%s" %(self.nome, self.telefone, self.empresa)) 

    def curtir(self):
        self.__curtidas += 1
        
    def obter_curtidas(self):
        return self.__curtidas
    
perfil = Perfil('Pedro Henrique', 'Não informado', 'Minecraft produções')
perfil.curtir()
perfil.curtir()
perfil.obter_curtidas()