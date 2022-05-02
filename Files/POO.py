from datetime import datetime

class Pessoa:
    ano_atual= int(datetime.strftime(datetime.now(), "%Y"))

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
        return self.ano_atual- self.idade


p1= Pessoa('Luiz', 29)
p2= Pessoa('João', 15)
p1.falar("Marvel")
p2.falar("DC")
p2.parar_falar()
p2.comer('amendoim')
p1.parar_falar()
p1.falar('Pokemon')
print(Pessoa.ano_atual)
print(p1.ano_nascimento())
print(p2.ano_nascimento())
# p1.comer('maça')
# p1.parar_comer()
# # p1.parar_comer()
# # p1.comer('maçã')
# p1.falar('Pokemon')
# p1.parar_falar()
# p1.parar_falar()
# p1.falar('Marvel')
# p1.comer('maça')