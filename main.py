#Impementação de algoritmo descrito em artigo: [17] OPFKA a Secure and Efficient Ordered-Physiological-Feature-based Key Agreement for Wireless Body Area Networks
from Modulos.IPI import Le_IPI
from Modulos.IEEE754Converter import Converter
from Modulos.ChaffPoints import *
import numpy as np
import hashlib

if __name__ == "__main__":

    Limite = 10
    #Sender:
    IDs = random.randint(0,150)
    IDr = random.randint(0,150)
    while(IDr==IDs):
        IDr = random.randint(0, 150)
    IPIs_Sender = Le_IPI(0,4)
    IPIs_Sender_Concatenados =[]
    print(len(IPIs_Sender))
    for i in range (0,90,3):
        Binario1 = Converter(IPIs_Sender[i])
        Binario2 = Converter(IPIs_Sender[i+1])
        Binario3 = Converter(IPIs_Sender[i+2])
        IPIs_Sender_Concatenados.append(Binario1[28:32]+Binario2[28:32]+Binario3[28:32])
    # print(IPIs_Concatenados)
    CaracteristicasSender=[]
    for j in range(len(IPIs_Sender_Concatenados)):
        CaracteristicasSender.append(str(hashlib.sha1(IPIs_Sender_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(Hashs[j]," ",len(Hashs[j]))
        CaracteristicasSender[j]= (CaracteristicasSender[j][0:20])
        # print(Hashs[j]," ",len(Hashs[j]))
    print("\nCaracteristicas do Sender(Hashs): ",CaracteristicasSender," ",len(CaracteristicasSender),"\n")
    chaffpoints=generateChaffPoints(CaracteristicasSender,30)
    Cofre=[]
    Cofre.extend(CaracteristicasSender)
    Cofre.extend(chaffpoints)
    # print(Cofre)
    np.random.shuffle(Cofre)
    print("\nCofre de tamanho ",len(Cofre)," : ",Cofre)
    

    # receiver:
    # Receiver recebe IDs,IDr,Cofre e (nonce?)
    IPIs_receiver = Le_IPI(0,4)
    IPIs_Concatenados = []
    print(len(IPIs_receiver))
    for i in range(0, 90, 3):
        Binario1 = Converter(IPIs_receiver[i])
        Binario2 = Converter(IPIs_receiver[i+1])
        Binario3 = Converter(IPIs_receiver[i+2])
        IPIs_Concatenados.append(
            Binario1[28:32]+Binario2[28:32]+Binario3[28:32])
    # print(IPIs_Concatenados)
    Hashs = []
    for j in range(len(IPIs_Concatenados)):
        Hashs.append(str(hashlib.sha1(IPIs_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(Hashs[j], " ", len(Hashs[j]))
        Hashs[j] = (Hashs[j][0:20])
        # print(Hashs[j], " ", len(Hashs[j]))
    print("\nHashs: ", Hashs, " ", len(Hashs), "\n")

    Q = []

    for k in range(len(Cofre)):
        if Cofre[k] in Hashs:
            Q.append(str(k))
    print("Indices chave Q: ", Q)
    # Forma abaixo de encontrar hash de Q pode estar errada:
    Aux = ""
    for s in Q:
        Aux = Aux + str(hashlib.sha1(s.encode('utf-8')).hexdigest()) #Algoritmo concatena hash do valor de cada elemento da lista em uma variavel
    K = str(hashlib.sha1(Aux.encode('utf-8')).hexdigest()) #Por fim faz o hash da variavel.
    print("Hash K :", K)
#Receiver envia para Sender mensagem IDr,IDs, MAC(K,I / Q / IDr)
#Sender realizar computações
    ContadorLimite=0
    for i in Q:
        if Cofre[int(i)] in CaracteristicasSender:
            ContadorLimite+=1
    if ContadorLimite>=Limite:
        print("ACORDO!")
    else:
        print("NAO ACORDO!")





        

