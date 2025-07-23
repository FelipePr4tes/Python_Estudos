class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('plim plim...')

    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada!')

    def correr(self):
        print('Vrummm...')

    def __str__(self):
        return f"{self.__class__.__name__}: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"


b1 = Bicicleta('verde', 'monark', 2000, 189)
b1.buzinar()
b1.correr()
b1.parar()

print(b1)
