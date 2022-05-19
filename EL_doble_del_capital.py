print("-------------------------------------------")
print("-------suma N primeros naturales-----------")
print("-------------------------------------------")

#entrada
C = int(input("digite la cantidad del capital: "))


#PROCESAMIENTO 
mes = 0 
i = 0.05
D = 2*C

while C < D:
    mes= mes + 1
    C = C * i + C

print(mes)
    


