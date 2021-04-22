import wfdb
import statistics
import tracemalloc
from Modulos.IPI import Le_IPI
from Modulos.IEEE754Converter import Converter
from Modulos.ChaffPoints import *
from Modulos.HMAC import *
import numpy as np
import hashlib

def memoryPeakStatistics():
    memoryPeakExtractFeatTransmitterArray = []
    memoryPeakExtractFeatReceiverArray = []
    memoryPeakGenerateLockVaultArray = []
    memoryPeakUnlockVaultArray = []
    memoryPeakFeatureAcknowledgementArray =[]
    totalMemoryPeakTransmitterArray = []
    totalMemoryPeakReceiverArray = []
    
   
    for i in range(1,91):
      
        if(i == 13 or i == 74):
            continue
        memoryPeakExtractFeatTransmitter, memoryPeakExtractFeatReceiver, memoryPeakGenerateLockVault, memoryPeakUnlockVault, memoryPeakFeatureAcknowledgement = OPFKAProtocolMemory(i)

        memoryPeakExtractFeatTransmitterArray.append(memoryPeakExtractFeatTransmitter/1024)
        memoryPeakExtractFeatReceiverArray.append(memoryPeakExtractFeatReceiver/1024)
        memoryPeakGenerateLockVaultArray.append(memoryPeakGenerateLockVault/1024)
        memoryPeakUnlockVaultArray.append(memoryPeakUnlockVault/1024)
        memoryPeakFeatureAcknowledgementArray.append(memoryPeakFeatureAcknowledgement/1024)
        totalMemoryPeakTransmitterArray.append(memoryPeakExtractFeatTransmitter/1024 + memoryPeakGenerateLockVault/1024 + memoryPeakFeatureAcknowledgement/1024)
        totalMemoryPeakReceiverArray.append(memoryPeakExtractFeatReceiver/1024 + memoryPeakUnlockVault/1024)

        print("\nMemory Peak to Extract Features on Transmitter: "+str(memoryPeakExtractFeatTransmitter/1024))
        print("Memory Peak to Extract Features on Receiver: "+str(memoryPeakExtractFeatReceiver/1024))
        print("Memory Peak to generate the locked vault on Transmitter: "+str(memoryPeakGenerateLockVault/1024))
        print("Memory Peak to unlock vault on Receiver: "+str(memoryPeakUnlockVault/1024))
        print("Memory Peak to verify positions on Transmitter: "+str(memoryPeakFeatureAcknowledgement/1024))
        print("Total memory peak Transmitter: "+str(memoryPeakExtractFeatTransmitter/1024 + memoryPeakGenerateLockVault/1024 + memoryPeakFeatureAcknowledgement/1024))
        print("Total memory peak Receiver: "+str(memoryPeakExtractFeatReceiver/1024 + memoryPeakUnlockVault/1024))

    print("\n---------------------")
    print("\nTotal statistics")

    print("\nMemory Peak to Extract Features on Transmitter")
    print("Mean: " + str(statistics.mean(memoryPeakExtractFeatTransmitterArray)))
    print("Standard Deviation: " + str(statistics.pstdev(memoryPeakExtractFeatTransmitterArray)))
    print("Variance: " + str(statistics.pvariance(memoryPeakExtractFeatTransmitterArray)))

    print("\nMemory Peak to Extract Features on Receiver")
    print("Mean: " + str(statistics.mean(memoryPeakExtractFeatReceiverArray)))
    print("Standard Deviation: " + str(statistics.pstdev(memoryPeakExtractFeatReceiverArray)))
    print("Variance: " + str(statistics.pvariance(memoryPeakExtractFeatReceiverArray)))

    print("\nMemory Peak to generate the locked vault on Transmitter")
    print("Mean: " + str(statistics.mean(memoryPeakGenerateLockVaultArray)))
    print("Standard Deviation: " + str(statistics.pstdev(memoryPeakGenerateLockVaultArray)))
    print("Variance: " + str(statistics.pvariance(memoryPeakGenerateLockVaultArray)))

    print("\nMemory Peak to unlock vault on Receiver")
    print("Mean: " + str(statistics.mean(memoryPeakUnlockVaultArray)))
    print("Standard Deviation: " + str(statistics.pstdev(memoryPeakUnlockVaultArray)))
    print("Variance: " + str(statistics.pvariance(memoryPeakUnlockVaultArray)))

    print("\nMemory Peak to verify positions on Transmitter:")
    print("Mean: " + str(statistics.mean(memoryPeakFeatureAcknowledgementArray)))
    print("Standard Deviation: " + str(statistics.pstdev(memoryPeakFeatureAcknowledgementArray)))
    print("Variance: " + str(statistics.pvariance(memoryPeakFeatureAcknowledgementArray)))

    print("\nTotal Memory Peak Transmitter")
    print("Mean: " + str(statistics.mean(totalMemoryPeakTransmitterArray)))
    print("Standard Deviation: " + str(statistics.pstdev(totalMemoryPeakTransmitterArray)))
    print("Variance: " + str(statistics.pvariance(totalMemoryPeakTransmitterArray)))

    print("\nTotal Memory Peak Receiver")
    print("Mean: " + str(statistics.mean(totalMemoryPeakReceiverArray)))
    print("Standard Deviation: " + str(statistics.pstdev(totalMemoryPeakReceiverArray)))
    print("Variance: " + str(statistics.pvariance(totalMemoryPeakReceiverArray)))


    archive = open('analysis/memoryStatistics.txt', 'w')

    archive.write("\nTotal statistics")

    archive.write("\n\nMemory Peak to Extract Features on Transmitter")
    archive.write("\nMean: " + str(round(statistics.mean(memoryPeakExtractFeatTransmitterArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(memoryPeakExtractFeatTransmitterArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(memoryPeakExtractFeatTransmitterArray), 2)).replace('.', ','))

    archive.write("\n\nMemory Peak to Extract Features on Receiver")
    archive.write("\nMean: " + str(round(statistics.mean(memoryPeakExtractFeatReceiverArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(memoryPeakExtractFeatReceiverArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(memoryPeakExtractFeatReceiverArray), 2)).replace('.', ','))

    archive.write("\n\nMemory Peak to generate the locked vault on Transmitter")
    archive.write("\nMean: " + str(round(statistics.mean(memoryPeakGenerateLockVaultArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(memoryPeakGenerateLockVaultArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(memoryPeakGenerateLockVaultArray), 2)).replace('.', ','))

    archive.write("\n\nMemory Peak to unlock vault on Receiver")
    archive.write("\nMean: " + str(round(statistics.mean(memoryPeakUnlockVaultArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(memoryPeakUnlockVaultArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(memoryPeakUnlockVaultArray), 2)).replace('.', ','))

    archive.write("\n\nMemory Peak to to verify positions on Transmitter:")
    archive.write("\nMean: " + str(round(statistics.mean(memoryPeakFeatureAcknowledgementArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(memoryPeakFeatureAcknowledgementArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(memoryPeakFeatureAcknowledgementArray), 2)).replace('.', ','))

    archive.write("\n\nTotal Memory Peak Transmitter")
    archive.write("\nMean: " + str(round(statistics.mean(totalMemoryPeakTransmitterArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(totalMemoryPeakTransmitterArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(totalMemoryPeakTransmitterArray), 2)).replace('.', ','))

    archive.write("\n\nTotal Memory Peak Receiver")
    archive.write("\nMean: " + str(round(statistics.mean(totalMemoryPeakReceiverArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(totalMemoryPeakReceiverArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(totalMemoryPeakReceiverArray), 2)).replace('.', ','))

    archive.close()
def OPFKAProtocolMemory(Paciente):

    # Definindo variáveis para coletar tempo
    memoryPeakExtractFeatTransmitter = 0
    memoryPeakExtractFeatReceiver = 0
    memoryPeakGenerateLockVault = 0
    memoryPeakUnlockVault = 0
    memoryPeakFeatureAcknowledgement = 0
    
    Limite = 10
    #Sender Gerando caracteristicas e criando cofre:
    # Gerando IDs e nonce
    nonce = random.randint(1, 150)
    IDs = str(random.randint(1, 150))
    IDr = str(random.randint(1, 150))
    while(IDr == IDs):
        IDr = str(random.randint(1, 150))

    IPIs_Sender = Le_IPI(0, 2, Paciente)
    IPIs_Sender_Concatenados = []
    print(len(IPIs_Sender))
    tracemalloc.start()
        
        # Juntando 3 IPIs
    for i in range(0, 36, 3):
        Binario1 = Converter(IPIs_Sender[i])
        Binario2 = Converter(IPIs_Sender[i+1])
        Binario3 = Converter(IPIs_Sender[i+2])
        IPIs_Sender_Concatenados.append(
            Binario1[28:32]+Binario2[28:32]+Binario3[28:32])

        # print(IPIs_Concatenados)
        # Fazendo hash de cada ipi e gerando caracteristica
    CaracteristicasSender = []
    for j in range(len(IPIs_Sender_Concatenados)):
        CaracteristicasSender.append(
            str(hashlib.sha1(IPIs_Sender_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(Hashs[j]," ",len(Hashs[j]))
        CaracteristicasSender[j] = (CaracteristicasSender[j][0:20])
        # print(Hashs[j]," ",len(Hashs[j]))
    # print("\nCaracteristicas do Sender(Hashs): ", CaracteristicasSender, " ", len(CaracteristicasSender), "\n")
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memoryPeakExtractFeatTransmitter = peak

    tracemalloc.start()
        
    # Gerando Chaffpoints e gerando cofre.
    chaffpoints = generateChaffPoints(CaracteristicasSender, 288)
    Cofre = []
    Cofre.extend(CaracteristicasSender)
    Cofre.extend(chaffpoints)
    # print(Cofre)
    np.random.shuffle(Cofre)
    #print("\nCofre de tamanho ", len(Cofre), " : ", Cofre)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memoryPeakGenerateLockVault = peak
    # receiver:
    # Receiver recebe IDs,IDr,Cofre e Nonce
    # Realizando leitura de IPIs e calculo de caracteristicas de receiver
    IPIs_receiver = Le_IPI(0, 2, Paciente)
    IPIs_Concatenados = []
    #print(len(IPIs_receiver))

    tracemalloc.start()
        
    # Juntando 3 ipis
    for i in range(0, 36, 3):
        Binario1 = Converter(IPIs_receiver[i])
        Binario2 = Converter(IPIs_receiver[i+1])
        Binario3 = Converter(IPIs_receiver[i+2])
        IPIs_Concatenados.append(
            Binario1[28:32]+Binario2[28:32]+Binario3[28:32])
    print(IPIs_Concatenados)

    # Caracteristicas do receiver (hashs de IPIs)
    Hashs = []
    for j in range(len(IPIs_Concatenados)):
        Hashs.append(
            str(hashlib.sha1(IPIs_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(Hashs[j], " ", len(Hashs[j]))
        Hashs[j] = (Hashs[j][0:20])
        # print(Hashs[j], " ", len(Hashs[j]))
    #print("\nHashs: ", Hashs, " ", len(Hashs), "\n")

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memoryPeakExtractFeatReceiver = peak
    # Fazendo comparação entre caracteristicas adquiridas em receiver e cofre de sender
    tracemalloc.start()
   
    Q = []
    I = []
    K = hashlib.sha1()
    for k in range(len(Cofre)):
        if Cofre[k] in Hashs:
            Q.append(Cofre[k])
            I.append(k)
            K.update(str(Cofre[k]).encode('utf-8'))
    #QConcatenado= (''.join(Q)) #Uso de join tem mesmo efeito de update acima em hashlib.
    #K = hashlib.sha1(QConcatenado.encode('utf-8'))
    #print("Caracteristicas Q:", Q)
    #print("Caracteristicas Q concatenadas: ",QConcatenado)
    #print("Indices de caracteristicas I: ", I)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memoryPeakUnlockVault = peak
    # Forma abaixo de encontrar hash de Q pode estar errada:
    # Aux = ""
    # for s in Q:
    #     Aux = Aux + str(hashlib.sha1(s.encode('utf-8')).hexdigest()) #Algoritmo concatena hash do valor de cada elemento da lista em uma variavel
    # K = str(hashlib.sha1(Aux.encode('utf-8')).hexdigest()) #Por fim faz o hash da variavel.
    print("Hash K :", K.hexdigest())
    #Receiver envia para Sender mensagem IDr,IDs, MAC(K,I / Q / IDr)
    ReceiverAck = CriaAck(K, I, Q, IDr)
    #Receiver envia {IDs, IDr, I, M AC(K, I|Q|IDr)} para sender
    #Sender recebe e realizar verificações:
    tracemalloc.start()
    ContadorLimite = 0
    for i in I:
        if Cofre[i] in CaracteristicasSender:
            ContadorLimite += 1

    if ContadorLimite >= Limite:
        #se maior gera chave K'
        Q_ = []
        for i in I:
            Q_.append(Cofre[i])
        Caracteristicas = (''.join(Q_))
        #print(Caracteristicas)
        K_ = hashlib.sha1(Caracteristicas.encode('utf-8'))
        if(CriaAck(K_, I, Q_, IDr) == ReceiverAck):
            #print("K_:", K_.hexdigest())
            #print("K:",K.hexdigest())
            #if(K_.hexdigest()==K.hexdigest()):
            #Sender enviar ACK2 para receiver
            Ack2 = CriaAck2(K_, str(nonce), IDs, IDr)
            print("ACORDO!")
        else:
            print("NAO ACORDO! MAC DIFERENTE")
    else:
        print("NAO ACORDO!, Limite abaixo")

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memoryPeakFeatureAcknowledgement = peak

    return memoryPeakExtractFeatTransmitter, memoryPeakExtractFeatReceiver, memoryPeakGenerateLockVault, memoryPeakUnlockVault, memoryPeakFeatureAcknowledgement


memoryPeakStatistics()
