from random import random

class Produto:
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor

#Um individuo é composto de quais produtos vão ser levados no carregamento
#E o objetivo é conseguir o indivíduo com melhor lucro.
class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        self.espacos = espacos      #todos os espaços dos produtos
        self.valores = valores      #todos os valores dos produtos
        self.limite_espacos = limite_espacos    #Limite do exemplo = 3m²
        self.nota_avaliacao = 0     #nota de um indivíduo de acordo aos outros
        self.espaco_usado = 0       #espaço que esse individuo ocupa
        self.geracao = geracao      #
        self.cromossomo = []        #sequencia de 0 e 1 pra dizer o que vai ser levado
        
        #inicializando o cromossomo com valores aleatórios (0s e 1s)
        for i in range(len(espacos)):
            if random() < 0.5:
                self.cromossomo.append('0')
            else: 
                self.cromossomo.append('1')
        
    #Definindo a nota de avaliação daquele individuo e 
    #Quanto ele usou de espaço
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == '1':
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
                
        if soma_espacos > self.limite_espacos:
            nota = 1
            
        self.nota_avaliacao = nota
        self.espaco_usado  = soma_espacos
        
    def crossover(self, outro_individuo):
        corte = round(random() * len(self.cromossomo))
        filho1 = outro_individuo.cromossomo[0: corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo[corte::]
        
        filhos = [Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1),
                  Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)]
        
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        
        return filhos
    
    def mutacao(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
                    
        return self

        

class AlgoritmoGenetico:
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        
    def initialize_populacap(self, espacos, valores, limites_espacos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, valores, limites_espacos))
            
        self.melhor_solucao = self.populacao[0] #inicializa qual melhor individuo, mas ainda será setado

    def ordenar_populacao(self):
        self.populacao = sorted(self.populacao, 
                            key = lambda populacao: populacao.nota_avaliacao,
                            reverse = True)
        
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo

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
    lista_produtos.append(Produto("Notebook Lenovo",0.498, 1999.90))
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
    
    return { 'espacos' : espacos, 'valores': valores, 'nomes' : nomes }

#######################################################
######################Função principal#################
    
if __name__ == '__main__':
    lista_produtos = append_produtos()
    
    dictValues = append_espaco_valores_nomes(lista_produtos)
    espacos = dictValues['espacos']
    valores = dictValues['valores']
    nomes = dictValues['nomes']
    
    limite = 3  #limite de 3m³ pra uma carga
    
    tamanho_populacao = 20
    ag = AlgoritmoGenetico(tamanho_populacao)
    ag.initialize_populacap(espacos, valores, limite)
    
    for individuo in ag.populacao:
        individuo.avaliacao()
    
    ag.ordenar_populacao()
    
    ag.melhor_individuo(ag.populacao[0])
    
    print(ag.melhor_solucao.cromossomo)
    print(ag.melhor_solucao.nota_avaliacao)
        
    

    
    
    
    

