aux = [[40,36,39,22,24],[1,2,3,4,5]]
aux2 = []
def mayor(valor):
    for i in range(len(valor)-1):
        if (i == 0):
            if(valor[i]>valor[i+1]):
                valor[i+1]=valor[i]
            else:
                valor[i+1]=valor[i+1]
        else:
            if(valor[i]>valor[i-1]+valor[i+1]):
                valor[i+1]>valor[i]
            else:
                valor[i+1]=valor[i-1]+valor[i+1]
    return(int(valor[-1]))
def rec(valor):
    for i in valor:
        aux2.append(mayor(i))
    sol =  mayor(aux2)
    return(sol)
print(rec(aux))

        
    
