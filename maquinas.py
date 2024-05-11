class Maquinas:
  def __init__(self,tipo,modelo,ano_fabricacao):
    self.tipo  =  tipo
    self.modelo = modelo
    self.ano_fabricacao = ano_fabricacao
    self.ligado = False

  def ligar(self):
    self.ligado = True
    print(f"{self.tipo} {self.modelo} Ligado.")

  def desligar(self):
    self.ligado = False
    print(f"{self.tipo} {self.modelo} Desligado.")