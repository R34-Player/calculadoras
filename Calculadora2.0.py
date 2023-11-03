import math
pi = 3.14159265
menu = """
Opciones...
[1] Apotema
[2] Angulos-Totales/Lado
[3] Diagonales-totales/Lado
[4] Angulo-Exterior
[5] Angulo-Interior
"""
siclo = int(1)
while siclo == 1:
    print(menu)
    op = int(input("Caso:"))

    #Apotema
    if op == 1:
        lados = float(input("Numero de lados: "))
        largo = float(input("Largo: "))
        teta = 360/(2*lados)
        tangente = float( math.tan(teta*pi/180))
        apotema = largo/(2*tangente)
        print("Apotema:", apotema)
        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break

    #Angulos-Totales/lado
    elif op == 2:
        lados = float(input("Numero de lados: "))
        at = (lados-2)*180
        al = at/lados
        print("Angulos totales: ", at)
        print("Angulo por lado", al)
        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break

    #Diagonales-totales/lado
    elif op == 3:
        lados = int(input("Numero de lados: "))
        diag = lados-3
        diagt = (lados*diag)/2
        print("Diagonales desde un vertice: ", diag)
        print("Diagonales totales", diagt)
        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break

    elif op == 4:
        ama = float(input("Angulo mayor"))
        ame = float(input("Angulo menor"))
        ae = (ama-ame)/2
        print("Angulo exterior: ", ae)
        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break

    elif op == 5:
        ama = float(input("Angulo mayor"))
        ame = float(input("Angulo menor"))
        ae = (ama+ame)/2
        print("Angulo interior: ", ae)
        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break
    #Error
    else:
        print("error")
        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break
