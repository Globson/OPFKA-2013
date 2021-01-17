import wfdb
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from scipy import signal

for i in range(5):
    record = wfdb.rdrecord('samples/'+str(i+1), physical=False, channel_names= ['avf'])
    print(len(record.d_signal))
    print(record.sig_name)
    print(record.fs)
    
    sig = []
    freq = []
    seg = [0]
    for i in range(len(record.d_signal)):
        sig.extend(record.d_signal[i])
        freq.append(i)

        if((i+1) % record.fs == 0):
            seg.append((i+1)/record.fs)
    print(seg)
    peaks, _ = find_peaks(sig, height=10000) #funcao detecta picos,adiciona em vetor indices de picos.
    for i in peaks:
        print("Pico: ",i)
        print(sig[i])
    plt.plot(sig)
    plt.show()
    #y = signal.filtfilt(b, a, sig)
    b, a = signal.butter(10, 0.05)
    zi = signal.lfilter_zi(b, a)
    z, _ = signal.lfilter(b, a, sig, zi=zi*sig[0])
    y = signal.filtfilt(b, a, sig)
    #plt.plot(sig)
    plt.plot(y)
    #plt.plot(z)
    plt.show()
