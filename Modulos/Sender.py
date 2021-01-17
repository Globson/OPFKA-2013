from IPI import Le_IPI
from IEEE754Converter import Converter
from ChaffPoints import *
import numpy as np
import hashlib

def Sender():
    IDs = random.randint(0, 150)
    IDr = random.randint(0, 150)
    while(IDr == IDs):
         IDr = random.randint(0, 150)
    IPIs_Sender = Le_IPI(0, 4)
    IPIs_Sender_Concatenados = []
    print(len(IPIs_Sender))
    for i in range(0, 90, 3):
        Binario1 = Converter(IPIs_Sender[i])
        Binario2 = Converter(IPIs_Sender[i+1])
        Binario3 = Converter(IPIs_Sender[i+2])
        IPIs_Sender_Concatenados.append(
            Binario1[28:32]+Binario2[28:32]+Binario3[28:32])
    # print(IPIs_Concatenados)
    CaracteristicasSender = []
    for j in range(len(IPIs_Sender_Concatenados)):
        CaracteristicasSender.append(
            str(hashlib.sha1(IPIs_Sender_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(Hashs[j]," ",len(Hashs[j]))
        CaracteristicasSender[j] = (CaracteristicasSender[j][0:20])
        # print(Hashs[j]," ",len(Hashs[j]))
    print("\nCaracteristicas do Sender(Hashs): ", CaracteristicasSender, " ", len(CaracteristicasSender),"\n")
    chaffpoints = generateChaffPoints(CaracteristicasSender, 30)
    Cofre = []
    Cofre.extend(CaracteristicasSender)
    Cofre.extend(chaffpoints)
    # print(Cofre)
    np.random.shuffle(Cofre)
    print("\nCofre de tamanho ", len(Cofre), " : ", Cofre)
    
