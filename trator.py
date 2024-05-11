from maquinas import Maquinas

class Trator(Maquinas):
        # Construtor da classe filha
    def __init__(self,tipo,modelo,ano_fabricacao, potencia_motor, capacidade_carga):
       super().__init__(tipo,modelo,ano_fabricacao)
       self.potencia_motor = potencia_motor
       self.capacidade_carga = capacidade_carga


    def imprimir(self):
            print(f"Tipo: {self.tipo}")
            print(f'Modelo: {self.modelo}')
            print(f'Ano de Fabricação: {self.ano_fabricacao}')
            print(f'Potência do Motor: {self.potencia_motor}Cavalos')
            print(f'Capacidade de Carga: {self.capacidade_carga}Kg')

    def arar(self):
        if self.ligado:
                print(f"{self.tipo} {self.modelo} arando.")
        else:
                print("Trator está ocioso")

    def transportar_carga(self):
        if self.ligado:
                print(f"{self.tipo} {self.modelo} transportando carga.")

        else:
                print("Trator está ocioso")