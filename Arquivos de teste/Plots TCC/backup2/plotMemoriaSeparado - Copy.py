import matplotlib.pyplot as plt
import numpy as np

width = 0.35

SMALL_SIZE = 13
MEDIUM_SIZE = 16
BIGGER_SIZE = 24

plt.rcParams['font.sans-serif'] = ['Times New Roman', 'sans-serif']

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title



labels_PSKA = ['Extração de\ncaracterísticas', 'Processamento\ndo cofre']
transmissor_PSKA = [218.75, 17.08]
receptor_PSKA = [218.75, 11.23]
transmissor_PSKA_std = [1.84, 2.68]
receptor_PSKA_std = [1.84, 1.7]

r1 = np.arange(len(labels_PSKA))
r2 = [x + width for x in r1]
plt.figure(figsize=(7,8))
plt.bar(r1, transmissor_PSKA, width, color='#d62728', yerr=transmissor_PSKA_std, label='Transmissor')
plt.bar(r2, receptor_PSKA, width, yerr=receptor_PSKA_std, label='Receptor')
plt.ylabel('Consumo de memória (KB)')
#plt.xlabel('Fases')
plt.margins(x=0.25)
plt.subplots_adjust(bottom=0.28, top=0.98, right=0.98, left=0.15)
plt.xticks([r + (width/2)+0.1 for r in range(len(labels_PSKA))], labels_PSKA, rotation=45, horizontalalignment='right')
plt.ylim([0,250])
#plt.title('Análise Empírica - Tempo de execução - PSKA')
plt.legend()
plt.savefig('memoriaPSKA.png')
plt.savefig('memoriaPSKA.svg')
#plt.show()


labels_EKA =['Extração de\ncaracterísticas', 'Processamento\nda chave', 'Compromisso e\ndescompromisso']
transmissor_EKA = [234.97, 8.22, 12.97]
receptor_EKA = [234.96, 8.21, 12.41]
transmissor_EKA_std = [0.01, 0.05, 0]
receptor_EKA_std = [0, 0, 0]

r1 = np.arange(len(labels_EKA))
r2 = [x + width for x in r1]
plt.figure(figsize=(7,8))
plt.bar(r1, transmissor_EKA, width, color='#d62728', yerr=transmissor_EKA_std, label='Transmissor')
plt.bar(r2, receptor_EKA, width, yerr=receptor_EKA_std, label='Receptor')
plt.ylabel('Consumo de memória (KB)')
#plt.xlabel('Fases')
plt.xticks([r + (width/2)+0.1 for r in range(len(labels_EKA))], labels_EKA, rotation=45, horizontalalignment='right')
#plt.title('Análise Empírica - Tempo de execução - EKA')
plt.subplots_adjust(bottom=0.28, top=0.98, right=0.98, left=0.15)
plt.ylim([0,250])
plt.legend()
plt.savefig('memoriaEKA.png')
plt.savefig('memoriaEKA.svg')
#plt.show()


labels_total = ['Transmissor', 'Receptor']
total_PSKA_means = [235.83, 229.97]
total_PSKA_std = [4.5, 3.53]
total_EKA_means = [256.15, 255.58]
total_EKA_std = [0.05, 0.0]

r1 = np.arange(len(labels_total))
r2 = [x + width for x in r1]
plt.figure(figsize=(12,6))
plt.bar(r1, total_PSKA_means, width, color='#d62728', yerr=total_PSKA_std, label='PSKA')
plt.bar(r2, total_EKA_means, width, yerr=total_EKA_std, label='EKA')
plt.ylabel('Consumo de memória (KB)')
plt.xlabel('Dispositivos')
plt.xticks([r + width/2 for r in range(len(labels_total))], labels_total)
#plt.title('Análise Empírica - Tempo de execução')
plt.margins(x=0.35)
plt.subplots_adjust(bottom=0.13, top=0.97, right=0.99, left=0.09)
plt.ylim([0,300])
plt.legend()
plt.savefig('memoriaTotal.png')
plt.savefig('memoriaTotal.svg')
#plt.show()