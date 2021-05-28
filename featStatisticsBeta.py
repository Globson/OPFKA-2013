import wfdb
import random
import time
from Modulos.IPI import *
from Modulos.IEEE754Converter import Converter
from Modulos.ChaffPoints import *
from Modulos.HMAC import *
import numpy as np
import hashlib

def featStatistics():
    ARArray = []
    FRRArray = []
    RRArray = []
    FARArray = []
    random.seed(time.time())

    for i in range(51):
        if i==12:
            continue

        AR, FRR = testFRR(i+1, 100, 50)
        ARArray.append(AR)
        FRRArray.append(FRR)

        RR, FAR = testFAR(i+1, 100, 50)
        RRArray.append(RR)
        FARArray.append(FAR)

        print("Acceptance Rate")
        print(str(AR*100)+"%")
        print("False Rejection Rate")
        print(str(FRR*100)+"%")
        print("---------------------")
        print("Rejection Rate")
        print(str(RR*100)+"%")
        print("False Acceptance Rate")
        print(str(FAR*100)+"%")
        print("------------------------------------------")

    print("------------------------------------------")
    print("------------------------------------------")
    print("------------------------------------------")
    print("Acceptance Rate: " + str((sum(ARArray)/len(ARArray))*100) + "%")
    print(str((sum(ARArray)/len(ARArray))*100)+"%")
    print("False Rejection Rate: " + str((sum(FRRArray)/len(FRRArray))*100) + "%")
    print("---------------------")
    print("Rejection Rate: " + str((sum(RRArray)/len(RRArray))*100) + "%")
    print("False Acceptance Rate: " + str((sum(FARArray)/len(FARArray))*100) + "%")

    archive = open('analysis/featStatistics.txt', 'w')
    archive.write("\nTotal Statistics")
    archive.write("\nAcceptance Rate: " + str((sum(ARArray)/len(ARArray))*100) + "%")
    archive.write("\nFalse Rejection Rate: " + str((sum(FRRArray)/len(FRRArray))*100) + "%")
    archive.write("\n---------------------")
    archive.write("\nRejection Rate: " + str((sum(RRArray)/len(RRArray))*100) + "%")
    archive.write("\nFalse Acceptance Rate: " + str((sum(FARArray)/len(FARArray))*100) + "%")
    archive.close()

def testFRR(recordNum, iterations, sampleVariation):
    count = 0
    countFRR = 0
    print(recordNum)
    IPIs_Sender = Le_IPI(0, 2, recordNum)
    IPIs_Sender_Concatenados = []
    print(len(IPIs_Sender))
    # Concatenando 3 IPIs
    for i in range(0, 36, 3):
        Binario1 = Converter(IPIs_Sender[i])
        Binario2 = Converter(IPIs_Sender[i+1])
        Binario3 = Converter(IPIs_Sender[i+2])
        IPIs_Sender_Concatenados.append(Binario1[28:32]+Binario2[28:32]+Binario3[28:32])


    IPIs_receiver = Le_IPI(0, 2, recordNum)
    IPIs_Concatenados = []
    print(len(IPIs_receiver))
    # Concatenando 3 ipis
    for i in range(0, 36, 3):
        Binario1 = Converter(IPIs_receiver[i])
        Binario2 = Converter(IPIs_receiver[i+1])
        Binario3 = Converter(IPIs_receiver[i+2])
        IPIs_Concatenados.append(Binario1[28:32]+Binario2[28:32]+Binario3[28:32])
    for i in range(iterations):
        #sampleFrom = random.randint(0, 800)
        ##recordTransmitter = wfdb.rdrecord('samples/'+str(recordNum), physical=False, sampfrom=sampleFrom, channel_names=['avf'])
        #recordTransmitter = wfdb.rdrecord('samples/patient'+recordNum+'/seg01', physical=False, sampfrom=0, channel_names=['V6-Raw'])
        ##recordReceiver = wfdb.rdrecord('samples/'+str(recordNum), physical=False, sampfrom=sampleFrom, channel_names=['avf'])
        #recordReceiver = wfdb.rdrecord('samples/patient'+recordNum+'/seg01', physical=False, sampfrom=0, channel_names=['V6-Raw'])
        if(OPFKAProtocol2(IPIs_Sender_Concatenados, IPIs_Concatenados)):
            count = count + 1
        else:
            countFRR = countFRR + 1
    return count/iterations, countFRR/iterations

def testFAR(recordNum, iterations, sampleVariation):
    count = 0
    countFAR = 0
    PacienteSender = recordNum
    IPIs_Sender = Le_IPI(0, 2, PacienteSender)
    IPIs_Sender_Concatenados = []
    print(len(IPIs_Sender))
    # Concatenando 3 IPIs
    for i in range(0, 36, 3):
        Binario1 = Converter(IPIs_Sender[i])
        Binario2 = Converter(IPIs_Sender[i+1])
        Binario3 = Converter(IPIs_Sender[i+2])
        IPIs_Sender_Concatenados.append(Binario1[28:32]+Binario2[28:32]+Binario3[28:32])
    for i in range(iterations):
        sampleFrom = random.randint(100, 150)
        PacienteReceiver = random.randint(1, 90)
        while (PacienteSender == PacienteReceiver) or (PacienteReceiver == 13) or (PacienteReceiver == 74) :
             PacienteReceiver = random.randint(1, 90)
        ##recordTransmitter = wfdb.rdrecord('samples/'+str(recordNumT), physical=False, sampfrom=sampleFrom, channel_names=['avf'])
        # recordTransmitter = wfdb.rdrecord('samples/patient'+recordNumT+'/seg01', physical=False, sampfrom=0, channel_names=['V6-Raw'])
        ##recordReceiver = wfdb.rdrecord('samples/'+str(recordNumR), physical=False, sampfrom=sampleFrom, channel_names=['avf'])
        # recordReceiver = wfdb.rdrecord('samples/patient'+recordNumR+'/seg01', physical=False, sampfrom=0, channel_names=['V6-Raw'])
        IPIs_receiver = Le_IPI(0, 2, PacienteReceiver)
        IPIs_Concatenados = []
        print(len(IPIs_receiver))
        # Concatenando 3 ipis
        for i in range(0, 36, 3):
            Binario1 = Converter(IPIs_receiver[i])
            Binario2 = Converter(IPIs_receiver[i+1])
            Binario3 = Converter(IPIs_receiver[i+2])
            IPIs_Concatenados.append(Binario1[28:32]+Binario2[28:32]+Binario3[28:32])
        if(OPFKAProtocol2(IPIs_Sender_Concatenados, IPIs_Concatenados, Limite=10)):
            countFAR = countFAR + 1
        else:
            count = count + 1
    return count/iterations, countFAR/iterations

def OPFKAProtocol(PacienteSender, PacienteReceiver, Limite = 10):

    '''if(Paciente==13 or Paciente==74):
        continue'''
    #Limite = 10
    # Paciente = 90


    #Sender:
    # Gerando IDs e nonce
    nonce = random.randint(1, 150)
    IDs = str(random.randint(1,150))
    IDr = str(random.randint(1,150))
    while(IDr==IDs):
        IDr = str(random.randint(1, 150))

    IPIs_Sender = Le_IPI(0,2,PacienteSender)
    IPIs_Sender_Concatenados =[]
    print(len(IPIs_Sender))

    # Concatenando 3 IPIs
    for i in range (0,36,3):
        Binario1 = Converter(IPIs_Sender[i])
        Binario2 = Converter(IPIs_Sender[i+1])
        Binario3 = Converter(IPIs_Sender[i+2])
        IPIs_Sender_Concatenados.append(Binario1[28:32]+Binario2[28:32]+Binario3[28:32])


    # print(IPIs_Concatenados)
    # Fazendo hash de cada ipi e gerando caracteristica
    CaracteristicasSender=[]
    for j in range(len(IPIs_Sender_Concatenados)):
        CaracteristicasSender.append(str(hashlib.sha1(IPIs_Sender_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(CaracteristicasSender[j]," ",len(CaracteristicasSender[j]))
        CaracteristicasSender[j]= (CaracteristicasSender[j][0:20])
        # print(CaracteristicasSender[j]," ",len(CaracteristicasSender[j]))
    #print("\nCaracteristicas do Sender(Hashs): ",CaracteristicasSender," ",len(CaracteristicasSender),"\n")



    # Gerando Chaffpoints e gerando cofre.
    chaffpoints=generateChaffPoints(CaracteristicasSender,288)
    Cofre=[]
    Cofre.extend(CaracteristicasSender)
    Cofre.extend(chaffpoints)
    # print(Cofre)
    np.random.shuffle(Cofre)
    #print("\nCofre de tamanho ",len(Cofre)," : ",Cofre)

    # receiver:
    # Receiver recebe IDs,IDr,Cofre e Nonce
    # Realizando leitura de IPIs e calculo de caracteristicas de receiver
    IPIs_receiver = Le_IPI(0,2,PacienteReceiver)
    IPIs_Concatenados = []
    print(len(IPIs_receiver))

    # Concatenando 3 ipis 
    for i in range(0, 36, 3):
        Binario1 = Converter(IPIs_receiver[i])
        Binario2 = Converter(IPIs_receiver[i+1])
        Binario3 = Converter(IPIs_receiver[i+2])
        IPIs_Concatenados.append(Binario1[28:32]+Binario2[28:32]+Binario3[28:32])
    print(IPIs_Concatenados)

    # Caracteristicas do receiver (hashs de IPIs)
    CaracteristicasReceiver = []
    for j in range(len(IPIs_Concatenados)):
        CaracteristicasReceiver.append(str(hashlib.sha1(IPIs_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(CaracteristicasReceiver[j], " ", len(CaracteristicasReceiver[j]))
        CaracteristicasReceiver[j] = (CaracteristicasReceiver[j][0:20])
        # print(CaracteristicasReceiver[j], " ", len(CaracteristicasReceiver[j]))
    #print("\nCaracteristicasReceiver: ", CaracteristicasReceiver, " ", len(CaracteristicasReceiver), "\n")


    # Fazendo comparação entre caracteristicas adquiridas em receiver e cofre de sender
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
    #print("Caracteristicas Q:",Q)
    #print("Caracteristicas Q concatenadas: ",QConcatenado)
    #print("Indices de caracteristicas I: ", I)


    print("Hash K :", K.hexdigest())
    #Receiver envia para Sender mensagem IDr,IDs, MAC(K,I / Q / IDr)
    ReceiverAck = CriaAck(K, I, Q, IDr)
    #Receiver envia {IDs, IDr, I, M AC(K, I|Q|IDr)} para sender




    #Sender recebe e realizar verificações:
    ContadorLimite=0
    for i in I:
        if Cofre[i] in CaracteristicasSender:
            ContadorLimite+=1


    if ContadorLimite>=Limite:
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
            return True
        else:
            print("NAO ACORDO! MAC DIFERENTE")
            return False
    else:
        print("NAO ACORDO!, Limite abaixo")
        return False


def OPFKAProtocol2(IPIs_Sender_Concatenados, IPIs_Concatenados, Limite=10):
    '''if(Paciente==13 or Paciente==74):
        continue'''
    #Limite = 10
    # Paciente = 90

    #Sender:
    # Gerando IDs e nonce
    nonce = random.randint(1, 150)
    IDs = str(random.randint(1, 150))
    IDr = str(random.randint(1, 150))
    while(IDr == IDs):
        IDr = str(random.randint(1, 150))

    # IPIs_Sender = Le_IPI(0, 2, PacienteSender)

    # print(IPIs_Concatenados)
    # Fazendo hash de cada ipi e gerando caracteristica
    CaracteristicasSender = []
    for j in range(len(IPIs_Sender_Concatenados)):
        CaracteristicasSender.append(
            str(hashlib.sha1(IPIs_Sender_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(CaracteristicasSender[j]," ",len(CaracteristicasSender[j]))
        CaracteristicasSender[j] = (CaracteristicasSender[j][0:20])
        # print(CaracteristicasSender[j]," ",len(CaracteristicasSender[j]))
    #print("\nCaracteristicas do Sender(Hashs): ",CaracteristicasSender," ",len(CaracteristicasSender),"\n")

    # Gerando Chaffpoints e gerando cofre.
    chaffpoints = generateChaffPoints(CaracteristicasSender, 288)
    Cofre = []
    Cofre.extend(CaracteristicasSender)
    Cofre.extend(chaffpoints)
    # print(Cofre)
    np.random.shuffle(Cofre)
    #print("\nCofre de tamanho ",len(Cofre)," : ",Cofre)

    # receiver:
    # Receiver recebe IDs,IDr,Cofre e Nonce
    # Realizando leitura de IPIs e calculo de caracteristicas de receiver
    # IPIs_receiver = Le_IPI(0, 2, PacienteReceiver)
    
    # print(IPIs_Concatenados)

    # Caracteristicas do receiver (hashs de IPIs)
    CaracteristicasReceiver = []
    for j in range(len(IPIs_Concatenados)):
        CaracteristicasReceiver.append(
            str(hashlib.sha1(IPIs_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(CaracteristicasReceiver[j], " ", len(CaracteristicasReceiver[j]))
        CaracteristicasReceiver[j] = (CaracteristicasReceiver[j][0:20])
        # print(CaracteristicasReceiver[j], " ", len(CaracteristicasReceiver[j]))
    #print("\nCaracteristicasReceiver: ", CaracteristicasReceiver, " ", len(CaracteristicasReceiver), "\n")

    # Fazendo comparação entre caracteristicas adquiridas em receiver e cofre de sender
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
    #print("Caracteristicas Q:",Q)
    #print("Caracteristicas Q concatenadas: ",QConcatenado)
    #print("Indices de caracteristicas I: ", I)

    print("Hash K :", K.hexdigest())
    #Receiver envia para Sender mensagem IDr,IDs, MAC(K,I / Q / IDr)
    ReceiverAck = CriaAck(K, I, Q, IDr)
    #Receiver envia {IDs, IDr, I, M AC(K, I|Q|IDr)} para sender

    #Sender recebe e realizar verificações:
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
            return True
        else:
            print("NAO ACORDO! MAC DIFERENTE")
            return False
    else:
        print("NAO ACORDO!, Limite abaixo")
        return False

featStatistics()
