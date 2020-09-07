# _*_ coding: UTF-8 _*_
# -*- coding: UTF-8 -*-

import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Espessura da intrusão (Metros)
w=20.00
#Temperatura inicial do magma (Celsius)
T0=1250
#Difusividade (m²/s)
k=0.000001
#Lista com os resultados dos modelos
TT = []
#Definição do eixo horizontal do gráfico
#np.linspace(VALOR INICIAL, VALOR FINAL, NUMERO DE PONTOS)
eixo_x = np.linspace(0.0, 1000.0, 1000)

#Tempos para se modelar
#tempo = np.linspace(0.0, 315360000, 10)
#tempo = [value*31536000 for value in range(10,20)]
#tempo = np.arange(0, 3153600000, 315360000)
#tempo.append(0)
tempo = [0, 31536000, 31536000*5, 31536000*10, 31536000*25, 31536000*50, 31536000*100, 31536000*1000]

#Alimentando a quantidade de resultados na lista TT
for t in tempo:
	TT.append([])

i=0
for t in tempo:
    for x in eixo_x:
        X1 = ((w-x)/(2*math.sqrt(k*t)))
        X2 = ((w+x)/(2*math.sqrt(k*t)))
        y=(T0/2)*(math.erf(X1)+math.erf(X2))
        TT[i].append(y)
    i = i +1

fig, ax = plt.subplots()

j = 0
for temperatura in TT:
    label_text = str(tempo[j]/31536000)+' anos'
    ax.plot(eixo_x, temperatura, label=label_text)
    j = j + 1

ax.set(xlabel="Profundidade (Metros)", ylabel='Temperatura (Celsius)', title='Temperatura x Tempo')
ax.grid()
ax.legend()
plt.show()