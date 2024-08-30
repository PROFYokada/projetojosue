class Livro:
    def __init__(self, titulo, autor, ano_Publicacao, preco):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_Publicacao
        self.__preco = preco
    
    #Get e set de titulo
    def get_titulo(self):
        return self.__titulo
    def set_titulo(self, nova_titulo):
        self.__titulo = nova_titulo
    
    #Get e set de autor
    def get_autor(self):
        return self.__autor
    def set_autor(self, novo_autor):
        self.__autor = novo_autor

    #Get e Set de Ano
    def get_ano_publicacao(self):
        return self.__ano_publicacao
    def set_ano_publicacao(self, novo_ano_publicacao):
        self.__ano_publicacao = novo_ano_publicacao

    #Get e set de preço
    def get_preco(self):
        return self.__preco
    def set_preco(self, novo_preco):
        self.__preco = novo_preco

# Criando uma instância de Livro
meu_livro = Livro("1984", "George Orwell", 1949, 40.00)

# Acessando os atributos através dos getters
print("Título:", meu_livro.get_titulo())
print("Autor:", meu_livro.get_autor())
print("Ano de Publicação:", meu_livro.get_ano_publicacao())
print("Preço:", meu_livro.get_preco())

# Modificando os atributos através dos setters
meu_livro.set_titulo("A Revolução dos Bichos")
meu_livro.set_autor("George Orwell")
meu_livro.set_ano_publicacao(1945)
meu_livro.set_preco(35.00)

# Acessando os atributos modificados
print("\nApós as modificações:")
print("Título:", meu_livro.get_titulo())
print("Autor:", meu_livro.get_autor())
print("Ano de Publicação:", meu_livro.get_ano_publicacao())
print("Preço:", meu_livro.get_preco())

