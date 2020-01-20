import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv ("fortaleza.csv")

plt.plot(data.Ano, data.Fort)
plt.title("Geral")
plt.grid(True)
plt.xlabel("Ano")
plt.ylabel("Fortaleza")
plt.show()

plt.plot(data.Ano[:10], data.Fort[0:10])
plt.title("Primeiros 10")
plt.xticks(data.Ano[0:10], data.Ano[0:10], rotation = 'vertical')
plt.grid(True)
plt.xlabel("Ano")
plt.ylabel("Fortaleza")
plt.show()

#10 ultimos
plt.plot(data.Ano[141:], data.Fort[141:])
plt.title("Ultimos 10")
plt.grid(True)
plt.xlabel("Ano")
plt.ylabel("Fortaleza")
plt.show()

#boxplot
plt.boxplot(data.Fort)
plt.title("Boxplot")
plt.grid(True)
plt.show()

#grid e 30 primeiros
plt.plot(data.Ano[0:30], data.Fort[0:30])
plt.title("Grid e primeiros 30")
plt.grid(True)
plt.xticks(data.Ano[0:30], data.Ano[0:30], rotation = 'vertical')
plt.show()