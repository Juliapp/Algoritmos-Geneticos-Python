from random import random

class Produto:
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco,
        self.valor = valor

#Um individuo é composto de quais produtos vão ser levados no carregamento
#E o objetivo é conseguir o indivíduo com melhor lucro.
class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos    #Limite do exemplo = 3m²
        self.nota_avaliacao = 0     #nota de um indivíduo de acordo aos outros
        self.geracao = geracao
        self.cromossomo = []    #sequencia de 0 e 1 pra dizer o que vai ser levado
        
        #inicializando o cromossomo com valores aleatórios (0s e 1s)
        for i in range(len(espacos)):
            if random() < 0.5:
                self.cromossomo.append('0')
            else: 
                self.cromossomo.append('1')
        
#Função que retorna todos os produtos
def append_produtos():
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
    lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
    lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
    lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
    lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
    lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
    lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
    lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
    lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
    lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
    lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
    lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
    return lista_produtos

#Função que retorna o array de cada atributo
#Recebe uma lista de objetos da classe produto
def append_espaco_valores_nomes(lista_produtos):
    espacos = []
    valores = []
    nomes = []
    
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    
    return espacos, valores, nomes

#######################################################
######################Função principal#################
#######################################################
    
if __name__ == '__main__':
    lista_produtos = append_produtos()
    espacos, valores, nomes = append_espaco_valores_nomes(lista_produtos)
    print(nomes)
    

