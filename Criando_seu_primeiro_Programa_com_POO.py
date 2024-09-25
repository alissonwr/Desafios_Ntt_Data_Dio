class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor=cor,
        self.modelo=modelo,
        self.ano=ano,
        self.valor=valor

    def buzinar(self):
        print('bunizar')
    
    def parar(self):
        print('parando')

    def correr(self):
        print( 'correndo')

    # def __str__(self):
    #     return f"""{self.cor} {self.modelo} {self.ano} {self.valor}"""

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta('Preta', 'BMX', 1997, 1000)

b1.buzinar()
b1.parar()
b1.correr()

print(b1)


