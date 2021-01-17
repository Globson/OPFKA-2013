import wfdb
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from scipy import signal

IPIs = []
start_at=0
for i in range(4):
    record = wfdb.rdrecord('samplesnovos/Person_01/rec_'+str(i+1), physical=False, channel_names= ['ECG I filtered'])
    print(len(record.d_signal))
    print(record.sig_name)
    print(record.fs)  #frequencia
    frequency = record.fs
    sig = []
    freq = []
    seg = [0]
    for i in range(len(record.d_signal)):
        sig.extend(record.d_signal[i])
        freq.append(i)

        if((i+1) % record.fs == 0):
            seg.append((i+1)/record.fs)
    print(seg)
    peaks, _ = find_peaks(sig, height=90, distance = 300) #funcao detecta picos,adiciona em vetor indices de picos.
    for i in peaks:
        print("Pico: ",i)
        print(sig[i])
    for i in (peaks):
        IPIs.append(i)
    for i in range(start_at,len(IPIs)-1):
        IPIs[i] = (IPIs[i+1]-IPIs[i])/record.fs
    start_at = len(IPIs)-1
    del(IPIs[len(IPIs)-1])
    plt.plot(sig)
    plt.show()


print("IPIs em segundos: ",IPIs)
print("Quantidade de IPIs: ",len(IPIs))


    
   
