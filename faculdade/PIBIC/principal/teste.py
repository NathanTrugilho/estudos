from pysr import PySRRegressor

modelo = PySRRegressor.from_file('equacoes.pkl')
quantidade_equacoes = int(modelo.equations_.count()["equation"])

print(quantidade_equacoes)
print(modelo)