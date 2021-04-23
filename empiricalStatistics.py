import wfdb
import time
import statistics
import tracemalloc
from Modulos.IPI import Le_IPI
from Modulos.IEEE754Converter import Converter
from Modulos.ChaffPoints import *
from Modulos.HMAC import *
import numpy as np
import hashlib

def timeStatistics():
    timeExtractFeatTransmitterArray = []
    timeExtractFeatReceiverArray = []
    timeGenerateLockVaultArray = []
    timeUnlockVaultArray = []
    timeFeatureAcknowledgementArray = [] 
    totalTimeTransmitterArray = []
    totalTimeReceiverArray = []

    for i in range(1,91):
      
        if(i == 13 or i == 74):
            continue
        timeExtractFeatTransmitter, timeExtractFeatReceiver, timeGenerateLockVault, timeUnlockVault, timeFeatureAcknowledgement = OPFKAProtocolTime(i)

        timeExtractFeatTransmitterArray.append(timeExtractFeatTransmitter)
        timeExtractFeatReceiverArray.append(timeExtractFeatReceiver)
        timeGenerateLockVaultArray.append(timeGenerateLockVault)
        timeUnlockVaultArray.append(timeUnlockVault)
        timeFeatureAcknowledgementArray.append(timeFeatureAcknowledgement)
        totalTimeTransmitterArray.append(timeExtractFeatTransmitter + timeGenerateLockVault + timeFeatureAcknowledgement)
        totalTimeReceiverArray.append(timeExtractFeatReceiver + timeUnlockVault)

        print("\nTime to Extract Features on Transmitter: "+str(timeExtractFeatTransmitter))
        print("Time to Extract Features on Receiver: "+str(timeExtractFeatReceiver))
        print("Time to generate the locked vault on Transmitter: "+str(timeGenerateLockVault))
        print("Time to unlock vault on Receiver: "+str(timeUnlockVault))
        print("Time to verify positions on transmitter: "+str(timeFeatureAcknowledgement))
        print("Total time: "+str(timeExtractFeatTransmitter + timeExtractFeatReceiver + timeGenerateLockVault + timeUnlockVault + timeFeatureAcknowledgement))

    print("\n---------------------")
    print("\nTotal statistics")

    print("\nTime to Extract Features on Transmitter")
    print("Mean: " + str(statistics.mean(timeExtractFeatTransmitterArray)))
    print("Standard Deviation: " + str(statistics.pstdev(timeExtractFeatTransmitterArray)))
    print("Variance: " + str(statistics.pvariance(timeExtractFeatTransmitterArray)))

    print("\nTime to Extract Features on Receiver")
    print("Mean: " + str(statistics.mean(timeExtractFeatReceiverArray)))
    print("Standard Deviation: " + str(statistics.pstdev(timeExtractFeatReceiverArray)))
    print("Variance: " + str(statistics.pvariance(timeExtractFeatReceiverArray)))

    print("\nTime to generate the locked vault on Transmitter")
    print("Mean: " + str(statistics.mean(timeGenerateLockVaultArray)))
    print("Standard Deviation: " + str(statistics.pstdev(timeGenerateLockVaultArray)))
    print("Variance: " + str(statistics.pvariance(timeGenerateLockVaultArray)))

    print("\nTime to unlock vault on Receiver")
    print("Mean: " + str(statistics.mean(timeUnlockVaultArray)))
    print("Standard Deviation: " + str(statistics.pstdev(timeUnlockVaultArray)))
    print("Variance: " + str(statistics.pvariance(timeUnlockVaultArray)))

    print("\nTime to verify positions on transmitter")
    print("Mean: " + str(statistics.mean(timeFeatureAcknowledgementArray)))
    print("Standard Deviation: " + str(statistics.pstdev(timeFeatureAcknowledgementArray)))
    print("Variance: " + str(statistics.pvariance(timeFeatureAcknowledgementArray)))

    print("\nTotal Time Transmitter")
    print("Mean: " + str(statistics.mean(totalTimeTransmitterArray)))
    print("Standard Deviation: " + str(statistics.pstdev(totalTimeTransmitterArray)))
    print("Variance: " + str(statistics.pvariance(totalTimeTransmitterArray)))

    print("\nTotal Time Receiver")
    print("Mean: " + str(statistics.mean(totalTimeReceiverArray)))
    print("Standard Deviation: " + str(statistics.pstdev(totalTimeReceiverArray)))
    print("Variance: " + str(statistics.pvariance(totalTimeReceiverArray)))

    archive = open('analysis/empiricalStatistics.txt', 'w')

    archive.write("\nTotal statistics")

    archive.write("\n\nTime to Extract Features on Transmitter")
    archive.write("\nMean: " + str(round(statistics.mean(timeExtractFeatTransmitterArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(timeExtractFeatTransmitterArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(timeExtractFeatTransmitterArray), 2)).replace('.', ','))

    archive.write("\n\nTime to Extract Features on Receiver")
    archive.write("\nMean: " + str(round(statistics.mean(timeExtractFeatReceiverArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(timeExtractFeatReceiverArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(timeExtractFeatReceiverArray), 2)).replace('.', ','))

    archive.write("\n\nTime to generate the locked vault on Transmitter")
    archive.write("\nMean: " + str(round(statistics.mean(timeGenerateLockVaultArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(timeGenerateLockVaultArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(timeGenerateLockVaultArray), 2)).replace('.', ','))

    archive.write("\n\nTime to unlock vault on Receiver")
    archive.write("\nMean: " + str(round(statistics.mean(timeUnlockVaultArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(timeUnlockVaultArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(timeUnlockVaultArray), 2)).replace('.', ','))

    archive.write("\n\nTime to verify positions on transmitter")
    archive.write("\nMean: " + str(round(statistics.mean(timeFeatureAcknowledgementArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(timeFeatureAcknowledgementArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(timeFeatureAcknowledgementArray), 2)).replace('.', ','))

    archive.write("\n\nTotal Time Transmitter")
    archive.write("\nMean: " + str(round(statistics.mean(totalTimeTransmitterArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(totalTimeTransmitterArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(totalTimeTransmitterArray), 2)).replace('.', ','))

    archive.write("\n\nTotal Time Receiver")
    archive.write("\nMean: " + str(round(statistics.mean(totalTimeReceiverArray), 2)).replace('.', ','))
    archive.write("\nStandard Deviation: " + str(round(statistics.pstdev(totalTimeReceiverArray), 2)).replace('.', ','))
    archive.write("\nVariance: " + str(round(statistics.pvariance(totalTimeReceiverArray), 2)).replace('.', ','))

    archive.close()

def OPFKAProtocolTime(Paciente):

    # Definindo variáveis para coletar tempo
    timeExtractFeatTransmitter = 0
    timeExtractFeatReceiver = 0
    timeGenerateLockVault = 0
    timeUnlockVault = 0
    timeFeatureAcknowledgement = 0
    
    Limite = 10  
    # Gerando IDs e nonce
    nonce = random.randint(1, 150)
    IDs = str(random.randint(1, 150))
    IDr = str(random.randint(1, 150))
    while(IDr == IDs):
        IDr = str(random.randint(1, 150))


    #Sender Gerando caracteristicas e criando cofre:
    IPIs_Sender = Le_IPI(0, 2, Paciente)
    IPIs_Sender_Concatenados = []
    print(len(IPIs_Sender))
    
    #Sender Gerando caracteristicas e criando cofre:
    inicio = time.time()
    # Concatenando 3 IPIs
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
        # print(CaracteristicasSender[j]," ",len(CaracteristicasSender[j]))
        CaracteristicasSender[j] = (CaracteristicasSender[j][0:20])
        # print(CaracteristicasSender[j]," ",len(CaracteristicasSender[j]))
    # print("\nCaracteristicas do Sender(Hashs): ", CaracteristicasSender, " ", len(CaracteristicasSender), "\n")
    fim = time.time()
    timeExtractFeatTransmitter = fim - inicio
    

    inicio = time.time()
    # Gerando Chaffpoints e gerando cofre.
    chaffpoints = generateChaffPoints(CaracteristicasSender, 288)
    Cofre = []
    Cofre.extend(CaracteristicasSender)
    Cofre.extend(chaffpoints)
    # print(Cofre)
    np.random.shuffle(Cofre)
    #print("\nCofre de tamanho ", len(Cofre), " : ", Cofre)
    fim = time.time()
    timeGenerateLockVault = fim - inicio  



    # receiver:
    # Receiver recebe IDs,IDr,Cofre e Nonce
    # Realizando leitura de IPIs e calculo de caracteristicas de receiver
    IPIs_receiver = Le_IPI(0, 2, Paciente)
    IPIs_Concatenados = []
    #print(len(IPIs_receiver))

  
    inicio = time.time()
    # Concatenando 3 ipis
    for i in range(0, 36, 3):
        Binario1 = Converter(IPIs_receiver[i])
        Binario2 = Converter(IPIs_receiver[i+1])
        Binario3 = Converter(IPIs_receiver[i+2])
        IPIs_Concatenados.append(
            Binario1[28:32]+Binario2[28:32]+Binario3[28:32])
    print(IPIs_Concatenados)

    # Caracteristicas do receiver (hashs de IPIs)
    CaracteristicasReceiver = []
    for j in range(len(IPIs_Concatenados)):
        CaracteristicasReceiver.append(
            str(hashlib.sha1(IPIs_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(CaracteristicasReceiver[j], " ", len(CaracteristicasReceiver[j]))
        CaracteristicasReceiver[j] = (CaracteristicasReceiver[j][0:20])
        # print(CaracteristicasReceiver[j], " ", len(CaracteristicasReceiver[j]))
    #print("\nCaracteristicasReceiver: ", CaracteristicasReceiver, " ", len(CaracteristicasReceiver), "\n")
    fim = time.time()
    timeExtractFeatReceiver = fim - inicio



    # Fazendo comparação entre caracteristicas adquiridas em receiver e cofre de sender
    inicio = time.time()
    Q = []
    I = []
    K = hashlib.sha1()
    for k in range(len(Cofre)):
        if Cofre[k] in CaracteristicasReceiver:
            Q.append(Cofre[k])
            I.append(k)
            K.update(str(Cofre[k]).encode('utf-8'))
    #QConcatenado= (''.join(Q)) #Uso de join tem mesmo efeito de update acima em hashlib.
    #K = hashlib.sha1(QConcatenado.encode('utf-8'))
    #print("Caracteristicas Q:", Q)
    #print("Caracteristicas Q concatenadas: ",QConcatenado)
    #print("Indices de caracteristicas I: ", I)
    fim = time.time()
    timeUnlockVault = fim - inicio
    print("Hash K :", K.hexdigest())


    #Receiver envia para Sender mensagem IDr,IDs, MAC(K,I / Q / IDr)
    ReceiverAck = CriaAck(K, I, Q, IDr)
    #Receiver envia {IDs, IDr, I, M AC(K, I|Q|IDr)} para sender


    
    #Sender recebe e realizar verificações:
    inicio = time.time()
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
    fim = time.time()
    timeFeatureAcknowledgement = fim - inicio
    
    return timeExtractFeatTransmitter*1000, timeExtractFeatReceiver*1000, timeGenerateLockVault*1000, timeUnlockVault*1000, timeFeatureAcknowledgement*1000

timeStatistics()
