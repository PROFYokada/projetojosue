class Carro:
    def __init__(self, marca, modelo, ano, cor, preço):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preço = preço

    #Método get e set de marca
    def get_marca(self):
        return self.__marca
    def set_marca(self, nova_marca):
        self.__marca = nova_marca
    
    #Método get e set de Modelo
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    #Método get e set de Ano
    def get_ano(self):
        return self.__ano
    def set_ano(self, novo_ano):
        self.__ano = novo_ano
        
     #Método get e set de cor
    def get_cor(self):
        return self.__cor
    def set_cor(self, novo_cor):
        self.__cor = novo_cor
    
     #Método get e set de preço
    def get_preço(self):
        return self.__preço
    def set_preço(self, novo_preço):
        self.__preço = novo_preço
    
#Exemplo de uso da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020, "Preto", 50000)

#Obtendo os valores dos atributos
print("Marca:", meu_carro.get_marca())
print("Modelo:", meu_carro.get_modelo())
print("Ano:", meu_carro.get_ano())
print("Cor:", meu_carro.get_cor())
print("Preço:", meu_carro.get_preço())

#Alterando valores dos Atributos
meu_carro.set_modelo("Camry")
meu_carro.set_ano(2021)
meu_carro.set_cor("Branco")
meu_carro.set_preço(60000)

#Verificar as alterações
print("Novo modelo:", meu_carro.get_modelo())
print("Novo ano:", meu_carro.get_ano())
print("Novo cor:", meu_carro.get_cor())
print("Novo preço:", meu_carro.get_preço())