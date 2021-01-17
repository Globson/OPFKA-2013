import wfdb
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def Le_IPI(n,m):
    IPIs = []
    start_at = 0
    for i in range(n,m):
        record = wfdb.rdrecord('samplesnovos/Person_10/rec_'+str(i+1), physical=False, channel_names= ['ECG I filtered'])
        print(len(record.d_signal))
        print(record.sig_name)
        print(record.fs)  #frequencia
        sig = []
        for i in range(len(record.d_signal)):
            sig.extend(record.d_signal[i])
        peaks, _ = find_peaks(sig, height=90, distance = 300) #funcao detecta picos,adiciona em vetor indices de picos.
        # for i in peaks:
            # print("Pico: ",i)
            # print(sig[i])
        for i in (peaks):
            IPIs.append(i)
        for i in range(start_at, len(IPIs)-1):
            IPIs[i] = (IPIs[i+1]-IPIs[i])/record.fs
        start_at = len(IPIs)-1
        del(IPIs[len(IPIs)-1])
        plt.plot(sig)
        # plt.show()
    # print(IPIs)
    return IPIs
