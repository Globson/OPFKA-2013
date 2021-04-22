import random
# M chaff points
def generateChaffPoints(vetorHash,quant_chaff): 
    chaffpoints=[]
    for i in range(quant_chaff):
        while(1):
            chaffpoint=''
            for j in range(20):
                aux = random.randint(0, 15)
                if aux == 10:
                    chaffpoint = chaffpoint + 'a'
                elif aux == 11:
                    chaffpoint = chaffpoint + 'b'
                elif aux == 12:
                    chaffpoint = chaffpoint + 'c'
                elif aux == 13:
                    chaffpoint = chaffpoint + 'd'
                elif aux == 14:
                    chaffpoint = chaffpoint + 'e'
                elif aux == 15:
                    chaffpoint = chaffpoint + 'f'
                else:
                    chaffpoint = chaffpoint + str(aux)
            if chaffpoint not in vetorHash:
                chaffpoints.append(chaffpoint)
                break
    #print(quant_chaff," ChaffPoints: ",chaffpoints)   
    return chaffpoints
