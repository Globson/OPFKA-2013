import wfdb
import matplotlib.pyplot as plt
from scipy import signal
from statsmodels.nonparametric.smoothers_lowess import lowess

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
