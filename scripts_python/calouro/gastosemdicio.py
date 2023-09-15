def gastosemdicio(matriz):

#Usado para teste:  matriz = [['05/11/18', 'almoço', 20.15], ["10/11/18", "𝐶𝑖𝑛𝑒𝑚𝑎", 65.5], ['15/12/18', 'Festa fim de ano', 50.0], ['20/12/18', 'jantar', 30.0]]

    d = {}
    mes1 = -1

    for i in range(0, len(matriz)):

        termo = matriz[i]
        
        data = termo[0]
        mes = data[3:5]
        custo = termo[2]
        
        if mes1 == mes:
            custo += aux
        
        aux = custo
    
        mes1 = mes
    
        d[mes1] = custo

    return d

print(gastosemdicio([['05/11/18', 'almoço', 20.15], ["10/11/18", "𝐶𝑖𝑛𝑒𝑚𝑎", 65.5], ['15/12/18', 'Festa fim de ano', 50.0], ['20/12/18', 'jantar', 30.0], ['09/08/2004', 'aniversário', 100.0]]))