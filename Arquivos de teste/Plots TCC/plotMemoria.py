import matplotlib.pyplot as plt


labels_PSKA = ['PSKA Transmissor', 'PSKA Receptor']
labels_EKA =['EKA Transmissor', 'EKA Receptor']

total_PSKA_means = [235.83, 229.97]
extract_feat_PSKA_means = [218.75, 218.75]
generate_vault_PSKA_means = [17.08, 11.23]

total_PSKA_std = [4.5, 3.53]
extract_feat_PSKA_std = [1.84, 1.84]
generate_vault_PSKA_std = [2.68, 1.7]

total_EKA_means = [256.15, 255.58]
extract_feat_EKA_means = [234.97, 234.96]
commitment_phase_EKA_means = [12.97,  12.41]
#commitment_phase_EKA_means = [9,43,  8,87]
process_key_EKA_means = [8.22,  8.21]
#decommitment_phase_EKA_means = [3,54,  3,54]

total_EKA_std = [0.05, 0.0]
extract_feat_EKA_std = [0.01, 0]
commitment_phase_EKA_std = [0, 0]
#commitment_phase_EKA_std = [0, 0]
process_key_EKA_std = [0.05, 0]
#decommitment_phase_EKA_std = [0, 0]

width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

#ax.bar(labels_PSKA, total_PSKA_means, width=0.45, yerr=total_PSKA_std)
ax.bar(labels_PSKA, extract_feat_PSKA_means, width, yerr=extract_feat_PSKA_std, label='Extração de características')
ax.bar(labels_PSKA, generate_vault_PSKA_means, width, yerr=generate_vault_PSKA_std, bottom=extract_feat_PSKA_means,
       label='Processamento do cofre')

#ax.bar(labels_EKA, total_EKA_means, width=0.45, yerr=total_EKA_std)
ax.bar(labels_EKA, extract_feat_EKA_means, width, yerr=extract_feat_EKA_std, label='Extração de características')
ax.bar(labels_EKA, commitment_phase_EKA_means, width, yerr=commitment_phase_EKA_std, bottom=extract_feat_EKA_means, label='Fase de compromisso/descompromisso')
ax.bar(labels_EKA, process_key_EKA_means, width, yerr=process_key_EKA_std, bottom=[(a + b) for a, b in zip(commitment_phase_EKA_means, extract_feat_EKA_means)], label='Processamento da chave')
#ax.bar(labels_EKA, process_key_EKA_means, width, yerr=process_key_EKA_std, bottom=extract_feat_EKA_means, label='Processamento da chave')
#ax.bar(labels_EKA, decommitment_phase_EKA_means, width, yerr=decommitment_phase_EKA_std, bottom=process_key_EKA_means, label='Fase de descompromisso')

ax.set_ylabel('Consumo de memória (KB)')
ax.set_title('Análise Empírica')
ax.legend()


plt.show()