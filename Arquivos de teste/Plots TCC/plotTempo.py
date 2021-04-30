import matplotlib.pyplot as plt


labels_PSKA = ['PSKA Transmissor', 'PSKA Receptor']
labels_EKA =['EKA Transmissor', 'EKA Receptor']

total_PSKA_means = [46.2, 50.16]
extract_feat_PSKA_means = [36.58, 35.98]
generate_vault_PSKA_means = [9.62, 14.18]

total_PSKA_std = [5.35, 6.8]
extract_feat_PSKA_std = [4.11, 3.27]
generate_vault_PSKA_std = [1.91, 6.31]

total_EKA_means = [34.24, 35.02]
extract_feat_EKA_means = [30.74, 31.58]
commitment_phase_EKA_means = [0.28,  0.30]
#commitment_phase_EKA_means = [0.16,  0.18]
process_key_EKA_means = [3.22,  3.14]
#decommitment_phase_EKA_means = [0.12,  0.12]

total_EKA_std = [3.08, 3.31]
extract_feat_EKA_std = [3.04, 3.44]
commitment_phase_EKA_std = [0.37, 0.38]
#commitment_phase_EKA_std = [0.37, 0.38]
process_key_EKA_std = [0.41, 0.45]
#decommitment_phase_EKA_std = [0.33, 0.33]

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

ax.set_ylabel('Tempo de execução (ms)')
ax.set_title('Análise Empírica')
ax.legend()


plt.show()