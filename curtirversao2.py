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
    
#Criando nossa instância
perfil = Perfil('Pedro Henrique', 'Não informado', 'Minecraft produções')

#Chamar o método imprimir da instância
perfil.imprimir()

#Curtir o perfil duas vezes
perfil.curtir()
perfil.curtir()

#Imprimir o número de curtidas
print("Curtidas:%d" % perfil.obter_curtidas())