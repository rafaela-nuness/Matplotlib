import matplotlib.pyplot as plt

dias = ['Segunda', 'Terça', 'Quarta', 'Quinta',
        'Sexta', 'Sábado', 'Domingo']

vendas = [1200, 1450, 1100, 1800, 3200, 4100, 2300]

plt.bar(dias, vendas)

plt.title('Vendas da Semana')
plt.xlabel('Dia')
plt.ylabel('Vendas')

plt.show()