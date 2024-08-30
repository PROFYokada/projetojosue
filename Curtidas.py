class Perfil(object):
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0
        
    def imprimir(self):
        print("Nome:%s, Telefone:%s, Empresa:%s" % (self.nome, self.telefone, self.empresa))

    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas

#Criar uma instancia    
perfil = Perfil('Luiz','Não informado','Gerson Produções')

#Chamar o método imprimir da instancia
perfil.imprimir()

#Curtir o perfil duas vezes
perfil.curtir()
perfil.curtir()

#Imprimir o numero de curtidas
print("Curtidas:%d" % perfil.obter_curtidas())
    


    