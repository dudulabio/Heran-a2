from maquinas import Maquinas

class Colheitadeira(Maquinas):
        # Construtor da classe filha
    def __init__(self,tipo,modelo,ano_fabricacao,largura_trabalho, potencia_motor, capacidade):
       super().__init__(tipo,modelo,ano_fabricacao)
       self.largura_trabalho = largura_trabalho     
       self.potencia_motor = potencia_motor
       self.capacidade_carga = capacidade

    def imprimir(self):
         print(f"Tipo: {self.tipo}")
         print(f'Modelo: {self.modelo}')
         print(f'Ano de Fabricação: {self.ano_fabricacao}')
         print(f'largura de trabalho: {self.largura_trabalho} pés')
         print(f'Potência do Motor: {self.potencia_motor} Cavalos')
         print(f'Capacidade de Carga: {self.capacidade_carga} Kg')

    def colhendo(self):
        if self.ligado:
                print(f"{self.tipo} {self.modelo} Colhendo.")
        else:
                print("Colheitadeira está em tempo Ocioso")

    def descarregando(self):
        if self.ligado:
                print(f"{self.tipo} {self.modelo} Descarregando.")

        else:
                print("Colheitadeira está em tempo Ocioso")