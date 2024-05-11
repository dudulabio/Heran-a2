##(self,tipo,modelo,ano_fabricacao, potencia_motor, capacidade_carga):
##(self,tipo,modelo,ano_fabricacao,largura_trabalho, potencia_motor, capacidade):

from trator import Trator
from colheitadeira import Colheitadeira

trator1= Trator(tipo="Trator",modelo="John Deere 9540R",ano_fabricacao=2023, potencia_motor= 540 , capacidade_carga = 29000)

colheitadeira1= Colheitadeira(tipo = "Colheitadeira PG-9", modelo = "John Deere X9", ano_fabricacao = 2023, largura_trabalho = 50,potencia_motor= 600,capacidade= 18000)

print('========================')
trator1.imprimir()
trator1.arar()
trator1.transportar_carga()
print('========================')
colheitadeira1.imprimir()
colheitadeira1.colhendo()
colheitadeira1.descarregando()

print('========================')