import math

class Circle:
    def __init__(self, center, radius):
        self.center = center  
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def test_pertencente(self, point):
        distance = math.sqrt((point[0] - self.center[0]) ** 2 + (point[1] - self.center[1]) ** 2)
        return distance <= self.radius

c1 = Circle((2, 2), 3)
print(c1.perimeter())  
print(c1.area())       
print(c1.test_pertencente((0, 0)))  
print(c1.test_pertencente((0, -1)))  

class Domino:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def mostrar_pontos(self):
        print(f"Lado A: {self.a}, Lado B: {self.b}")

    def value(self):
        return self.a + self.b

    def __str__(self):
        return f"Domino({self.a}, {self.b})"

d1 = Domino(2, 6)
d2 = Domino(4, 3)
d1.mostrar_pontos()
d2.mostrar_pontos()
print("Total de pontos:", d1.value() + d2.value())
print(d1)

import datetime

class Funcionario:
    def __init__(self, id_num, sobrenome, nome, data_nascimento, data_admissao, salario):
        self.id_num = id_num
        self.sobrenome = sobrenome
        self.nome = nome
        self.data_nascimento = datetime.datetime(*data_nascimento)
        self.data_admissao = datetime.datetime(*data_admissao)
        self.salario = salario

    def idade(self):
        return datetime.datetime.now().year - self.data_nascimento.year

    def tempo_de_casa(self):
        return datetime.datetime.now().year - self.data_admissao.year

    def aumento_de_salario(self):
        anos = self.tempo_de_casa()
        if anos < 5:
            self.salario *= 1.02
        elif anos < 10:
            self.salario *= 1.05
        else:
            self.salario *= 1.10

    def mostrar_funcionario(self):
        print(f"Número pessoal: {self.id_num}, Sobrenome: {self.sobrenome}, Nome: {self.nome}, Idade: {self.idade()}, Tempo de casa: {self.tempo_de_casa()}, Salário em €: {self.salario}")

agente = Funcionario('007', 'Bond', 'James', (11, 11, 1970), (7, 4, 1995), 7500)
agente.aumento_de_salario()
agente.mostrar_funcionario()

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Erro: Saldo insuficiente!")
        else:
            self.__saldo -= valor

    def exibir_saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nome):
        if nome == "":
            print("Erro: Nome do titular não pode ser vazio!")
        else:
            self.__titular = nome

    def __str__(self):
        return f"Conta de {self.__titular}"

c1 = ContaBancaria("Alice", 1000)
print(c1)
c1.depositar(500)
print(c1.exibir_saldo())
c1.sacar(2000)
c1.sacar(300)
print(c1.exibir_saldo())
c1.titular = ""

class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def _validar_preco(self, preco):
        return preco > 0

    def alterar_preco(self, novo_preco):
        if self._validar_preco(novo_preco):
            self.__preco = novo_preco
        else:
            print("Erro: O preço deve ser maior que zero.")

    def vender(self, quantidade):
        if quantidade > self.__estoque:
            print("Erro: Estoque insuficiente!")
        else:
            self.__estoque -= quantidade

    def reabastecer(self, quantidade):
        self.__estoque += quantidade

    def exibir_detalhes(self):
        print(f"Produto: {self.__nome}, Preço: {self.__preco}, Estoque: {self.__estoque}")

    def __str__(self):
        return f"Produto: {self.__nome}"

p = Produto("Caderno", 15.50, 10)
print(p)
p.alterar_preco(-5)
p.alterar_preco(20)
p.vender(5)
p.vender(10)
p.reabastecer(15)
p.exibir_detalhes()