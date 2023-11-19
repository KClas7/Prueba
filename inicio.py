print("Prueba de Suma Basica\n")
num1 = int(input("Ingrese el primer numero: "))
while not num1:
    try:
        print("\n DEBE DE INGRESAR EL DATO \n")
        num1 = int(input("Ingrese el primer numero: "))
    except:
        num1 = 0
num2 = int(input("Ingrese el segundo numero: "))
sumaT = float((num1 + num2)/2)
if(sumaT >= 7):
    print("\nAPROVADO\n")
    print("El resultado del promedio entre ",num1," y ",num2," es: ",sumaT)
elif(sumaT < 7):
    print("\nREPROVADO\n")
    print("El resultado del promedio entre ",num1," y ",num2," es: ",sumaT)
else:
    print("Error, ingrese datos, Por favor.")