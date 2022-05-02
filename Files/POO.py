from datetime import datetime
from random import *

class Pessoa:
    ano_atual= int(datetime.strftime(datetime.now(), "%Y"))

    #Métodos de instancia
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome= nome
        self.idade= idade
        self.comendo= comendo
        self.falando= falando
        variavel= 'Valor'
    # def outro_metodo(self):
    #     print(self.nome)
    #     print(variavel)
    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar enquanto está comendo.")
            return
        if self.falando:
            print(f"{self.nome} já está falando.")
            return
        print(f"{self.nome} está falando sobre {assunto}.")
        self.falando= True
    
    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando.")
            return
        print(f"{self.nome} parou de falar.")
        self.falando= False
    
    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return        
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo= True
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo= False
    def ano_nascimento(self):
        print(self.ano_atual- self.idade)
    
    #Método de classe
    @classmethod #não é referente à instancia em si, mas à classe
    def por_nascimento(cls, nome, ano_nascimento):
        idade= cls.ano_atual- ano_nascimento
        return cls(nome, idade)
    
    #Método estático
    @staticmethod
    def gerar_id(): #não recebe parametros(self, cls), pode receber mas não é obrigatório
        rand= randint(10000, 199999)
        return rand



# p1= Pessoa('Luiz', 29)
# p2= Pessoa('João', 15)
# p1.falar("Marvel")
# p2.falar("DC")
# p2.parar_falar()
# p2.comer('amendoim')
# p1.parar_falar()
# p1.falar('Pokemon')
# print(Pessoa.ano_atual)
# print(p1.ano_nascimento())
# print(p2.ano_nascimento())
# p1= Pessoa.por_nascimento('Luiz', 1987)
# p1= Pessoa('Luiz', 32)
# print(p1)
# print(p1.nome, p1.idade)
# p1.ano_nascimento()
# print(p1.gerar_id())
# print(Pessoa.gerar_id())

class Produto:
    def __init__(self, nome, preco):
        self.nome= nome
        self.preco= preco
    
    def desconto(self, percentual):
        self.preco= self.preco- (self.preco * (percentual/100))

    #Getter
    @property
    def preco(self):
        return self._preco
    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor= float(valor.replace('R$', ''))
        self._preco= valor

    #Getter
    @property
    def nome(self):
        return self._nome
    #Setter
    @nome.setter
    def nome(self, string):
        self._nome= string.replace('A', '@')


p1= Produto('Camisa', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2= Produto('CANECA', 'R$15')
# p2.desconto(10)
print(p2.preco)
print(p2.nome)
