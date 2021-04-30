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
transmissor_PSKA = [196.51, 57.75]
receptor_PSKA = [196.95, 78.54]
transmissor_PSKA_std = [7.6, 6.9]
receptor_PSKA_std = [7.62, 38.93]

r1 = np.arange(len(labels_PSKA))
r2 = [x + width for x in r1]
plt.figure(figsize=(7,8))
plt.bar(r1, transmissor_PSKA, width, color='#d62728', yerr=transmissor_PSKA_std, label='Transmissor')
plt.bar(r2, receptor_PSKA, width, yerr=receptor_PSKA_std, label='Receptor')
plt.ylabel('Tempo de execução (ms)')
#plt.xlabel('Fases')
plt.margins(x=0.25)
plt.subplots_adjust(bottom=0.28, top=0.98, right=0.99, left=0.15)
plt.xticks([r + (width/2) for r in range(len(labels_PSKA))], labels_PSKA, rotation=45, horizontalalignment='right')
plt.ylim([0,250])
#plt.title('Análise Empírica - Tempo de execução - PSKA')
plt.legend()
plt.savefig('tempoPSKA.png')
plt.savefig('tempoPSKA.svg')
#plt.show()


labels_EKA =['Extração de\ncaracterísticas', 'Processamento\nda chave', 'Compromisso e\ndescompromisso']
transmissor_EKA = [173.01, 27.73, 1.43]
receptor_EKA = [168.64, 27.63, 1.76]
transmissor_EKA_std = [15.17, 0.78, 0.03]
receptor_EKA_std = [14.27, 0.78, 0.03]

r1 = np.arange(len(labels_EKA))
r2 = [x + width for x in r1]
plt.figure(figsize=(7,8))
plt.bar(r1, transmissor_EKA, width, color='#d62728', yerr=transmissor_EKA_std, label='Transmissor')
plt.bar(r2, receptor_EKA, width, yerr=receptor_EKA_std, label='Receptor')
plt.ylabel('Tempo de execução (ms)')
#plt.xlabel('Fases')
plt.xticks([r + (width/2) for r in range(len(labels_EKA))], labels_EKA, rotation=45, horizontalalignment='right')
#plt.title('Análise Empírica - Tempo de execução - EKA')
plt.subplots_adjust(bottom=0.28, top=0.98, right=0.99, left=0.15)
plt.ylim([0,250])
plt.legend()
plt.savefig('tempoEKA.png')
plt.savefig('tempoEKA.svg')
#plt.show()


labels_total = ['Transmissor', 'Receptor']
total_PSKA_means = [254.26, 275.49]
total_PSKA_std = [14.42, 40.96]
total_EKA_means = [202.17, 198.03]
total_EKA_std = [14.87, 13.98]

r1 = np.arange(len(labels_total))
r2 = [x + width for x in r1]
plt.figure(figsize=(12,6))
plt.bar(r1, total_PSKA_means, width, color='#d62728', yerr=total_PSKA_std, label='PSKA')
plt.bar(r2, total_EKA_means, width, yerr=total_EKA_std, label='EKA')
plt.ylabel('Tempo de execução (ms)')
plt.xlabel('Dispositivos')
plt.xticks([r + width/2 for r in range(len(labels_total))], labels_total)
#plt.title('Análise Empírica - Tempo de execução')
plt.margins(x=0.35)
plt.subplots_adjust(bottom=0.13, top=0.97, right=0.99, left=0.09)
plt.ylim([0,350])
plt.legend()
plt.savefig('tempoTotal.png')
plt.savefig('tempoTotal.svg')
#plt.show()