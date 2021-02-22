# Impementação de algoritmo descrito em artigo: [17] OPFKA a Secure and Efficient Ordered-Physiological-Feature-based Key Agreement for Wireless Body Area Networks
from Modulos.IPI import Le_IPI
from Modulos.IEEE754Converter import Converter
from Modulos.ChaffPoints import *
from Modulos.HMAC import *
import numpy as np
import hashlib

if __name__ == "__main__":

    Limite = 10
    #Sender:
    # Gerando IDs e nonce
    nonce = random.randint(1, 150)
    IDs = str(random.randint(1,150))
    IDr = str(random.randint(1,150))
    while(IDr==IDs):
        IDr = random.randint(1, 150)

    
    IPIs_Sender = Le_IPI(0,2)
    IPIs_Sender_Concatenados =[]
    print(len(IPIs_Sender))

    # Juntando 3 IPIs
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
        # print(Hashs[j]," ",len(Hashs[j]))
        CaracteristicasSender[j]= (CaracteristicasSender[j][0:20])
        # print(Hashs[j]," ",len(Hashs[j]))
    print("\nCaracteristicas do Sender(Hashs): ",CaracteristicasSender," ",len(CaracteristicasSender),"\n")

    # Gerando Chaffpoints e gerando cofre.
    chaffpoints=generateChaffPoints(CaracteristicasSender,288)
    Cofre=[]
    Cofre.extend(CaracteristicasSender)
    Cofre.extend(chaffpoints)
    # print(Cofre)
    np.random.shuffle(Cofre)
    print("\nCofre de tamanho ",len(Cofre)," : ",Cofre)
    

    # receiver:
    # Receiver recebe IDs,IDr,Cofre e Nonce
    # Realizando leitura de IPIs e calculo de caracteristicas de receiver
    IPIs_receiver = Le_IPI(0,2)
    IPIs_Concatenados = []
    print(len(IPIs_receiver))

    # Juntando 3 ipis 
    for i in range(0, 36, 3):
        Binario1 = Converter(IPIs_receiver[i])
        Binario2 = Converter(IPIs_receiver[i+1])
        Binario3 = Converter(IPIs_receiver[i+2])
        IPIs_Concatenados.append(
            Binario1[28:32]+Binario2[28:32]+Binario3[28:32])
    # print(IPIs_Concatenados)

    # Caracteristicas do receiver (hashs de IPIs)
    Hashs = []
    for j in range(len(IPIs_Concatenados)):
        Hashs.append(str(hashlib.sha1(IPIs_Concatenados[j].encode('utf-8')).hexdigest()))
        # print(Hashs[j], " ", len(Hashs[j]))
        Hashs[j] = (Hashs[j][0:20])
        # print(Hashs[j], " ", len(Hashs[j]))
    print("\nHashs: ", Hashs, " ", len(Hashs), "\n")

    # Fazendo comparação entre caracteristicas adquiridas em receiver e cofre de sender
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
    print("Caracteristicas Q:",Q)
    #print("Caracteristicas Q concatenadas: ",QConcatenado)
    print("Indices de caracteristicas I: ", I)

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
        else:
            print("NAO ACORDO! MAC DIFERENTE")
    else:
        print("NAO ACORDO!, Limite abaixo")





        

