class Carro:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preco = preco
    
    #Get e set de Marca
    def get_marca(self):
        return self.__marca
    def set_marca(self, nova_marca):
        self.__marca = nova_marca
    
    #Get e set de modelo
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    #Get e Set de Ano
    def get_ano(self):
        return self.__ano
    def set_ano(self, novo_ano):
        self.__ano = novo_ano

    #Get e set de cor
    def get_cor(self):
        return self.__cor
    def set_cor(self, novo_cor):
        self.__cor = novo_cor

    #Get e set de preço
    def get_preco(self):
        return self.__preco
    def set_preco(self, novo_preco):
        self.__preco = novo_preco
    
#Exemplo de uso da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020, "Preto", 50000)

#Obtendo os valores dos atributos
print("Marca:", meu_carro.get_marca())
print("Modelo:", meu_carro.get_modelo())
print("Ano:", meu_carro.get_ano())
print("Cor:", meu_carro.get_cor())
print("Preço:", meu_carro.get_preco())

#Alterando valores dos Atributos
meu_carro.set_modelo("Camry")
meu_carro.set_ano(2021)
meu_carro.set_cor("Branco")
meu_carro.set_preco(60000)

#Verificar as alterações
print("Novo modelo:", meu_carro.get_modelo())
print("Novo ano:", meu_carro.get_ano())
print("Novo cor:", meu_carro.get_cor())
print("Novo preço:", meu_carro.get_preco())

class Estoque:
    def __init__(self):
        self.__carros = []  # Inicializa a lista de carros vazia

    def adicionar_carro(self, carro):
        self.__carros.append(carro)
        print(f"Carro {carro.get_marca()} {carro.get_modelo()} adicionado ao estoque.")

    def remover_carro(self, carro):
        if carro in self.__carros:
            self.__carros.remove(carro)
            print(f"Carro {carro.get_marca()} {carro.get_modelo()} removido do estoque.")
        else:
            print("Carro não encontrado no estoque.")

    def listar_carros(self):
        if self.__carros:
            print("Carros no estoque:")
            for carro in self.__carros:
                print(f"{carro.get_marca()} {carro.get_modelo()}")
        else:
            print("Estoque vazio.")

    def total_carros(self):
        return len(self.__carros)


# Exemplo de uso da classe Estoque
estoque = Estoque()

carro1 = Carro("Toyota", "Corolla", 2020, "Preto", 50000)
carro2 = Carro("Honda", "Civic", 2019, "Prata", 45000)

estoque.adicionar_carro(carro1)
estoque.adicionar_carro(carro2)

estoque.listar_carros()
print("Total de carros:", estoque.total_carros())

estoque.remover_carro(carro1)

estoque.listar_carros()
print("Total de carros:", estoque.total_carros())


