import math
pi = 3.14159265
menu = """
Opciones...
[1] Punto Medio
[2] Distancia entre dos puntos
[3] Pendiente de una recta
[4] Pendiente de una recta perpendicular a otra
[5] Angulo-Interior
[6] Angulo entre recta y el eje x
[7] Punto que divide una recta en una razon dada
[8] Ecuacion de una recta
"""
siclo = int(1)
while siclo == 1:
    print(menu)
    op = int(input("Caso:"))
#-----------------------------------------------------------------------
    #Punto medio
    if op == 1:
        x1 = float(input("Ingrese la coordenada x del primer punto: "))
        y1 = float(input("Ingrese la coordenada y del primer punto: "))
        x2 = float(input("Ingrese la coordenada x del segundo punto: "))
        y2 = float(input("Ingrese la coordenada y del segundo punto: "))

        # Calcular el punto medio
        midpoint_x = (x1 + x2) / 2
        midpoint_y = (y1 + y2) / 2
        midpoint = (midpoint_x, midpoint_y)

        # Imprimir el resultado
        print("El punto medio de la recta es:", midpoint)
        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break

    #Distancia entre dos puntos
    elif op == 2:
        # Solicitar las coordenadas de los dos puntos
        x1 = float(input("Ingrese la coordenada x del primer punto: "))
        y1 = float(input("Ingrese la coordenada y del primer punto: "))
        x2 = float(input("Ingrese la coordenada x del segundo punto: "))
        y2 = float(input("Ingrese la coordenada y del segundo punto: "))

        # Calcular la distancia
        distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

        # Imprimir el resultado
        print("La distancia entre los puntos es:", distancia)

        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break

    #Pendiente de una recta
    elif op == 3:
        # Solicitar las coordenadas de los dos puntos en la recta
        x1 = float(input("Ingrese la coordenada x del primer punto: "))
        y1 = float(input("Ingrese la coordenada y del primer punto: "))
        x2 = float(input("Ingrese la coordenada x del segundo punto: "))
        y2 = float(input("Ingrese la coordenada y del segundo punto: "))

        # Calcular la pendiente
        pendiente = (y2 - y1) / (x2 - x1)

        # Imprimir el resultado
        print("La pendiente de la recta es:", pendiente)

        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break

    #pendiente de una recta perpendicular a otra
    elif op == 4:
        # Solicitar la pendiente de la recta original
        pendiente_original = float(input("Ingrese la pendiente de la recta original: "))

        # Calcular la pendiente de la recta perpendicular
        pendiente_perpendicular = -1 / pendiente_original

        # Imprimir el resultado
        print("La pendiente de la recta perpendicular es:", pendiente_perpendicular)

        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break

    #angulo entre dos rectas
    elif op == 5:
        # Solicitar las pendientes de las dos rectas
        m1 = float(input("Ingrese la pendiente de la primera recta: "))
        m2 = float(input("Ingrese la pendiente de la segunda recta: "))

        # Calcular el ángulo entre las dos rectas
        angulo = math.atan(abs((m2 - m1) / (1 + m1 * m2)))

        # Convertir el resultado de radianes a grados
        angulo_grados = math.degrees(angulo)

        # Imprimir el resultado
        print("El ángulo entre las dos rectas es:", angulo_grados, "grados")

        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break
    
        #angulo entre dos rectas

    #Angulo entre recta y el eje x
    elif op == 6:
        # Solicitar la pendiente de la recta
        m = float(input("Ingrese la pendiente de la recta: "))

        # Calcular el ángulo entre la recta y el eje x
        angulo = math.atan(m)

        # Convertir el resultado de radianes a grados
        angulo_grados = math.degrees(angulo)

        # Imprimir el resultado
        print("El ángulo entre la recta y el eje x es:", angulo_grados, "grados")
        if siclo == 1:
            siclo = int(input("[1] continuar: "))
        else:
            break

    #Punto que divide una recta en una razon dada
    elif op == 7:
            # Solicitar las coordenadas de los dos puntos en la recta
            x1 = float(input("Ingrese la coordenada x del primer punto: "))
            y1 = float(input("Ingrese la coordenada y del primer punto: "))
            x2 = float(input("Ingrese la coordenada x del segundo punto: "))
            y2 = float(input("Ingrese la coordenada y del segundo punto: "))

            # Solicitar la razón en la que se divide la recta
            r = float(input("Ingrese la razón en la que se divide la recta: "))

            # Calcular el punto que divide la recta en la razón dada
            x = (r*x2 - r*x1) / (r + 1)
            y = (r*y2 - r*y1) / (r + 1)

            # Imprimir el resultado
            print("El punto que divide la recta en la razón", r, "es: (", x, ",", y, ")")
            if siclo == 1:
                siclo = int(input("[1] continuar: "))
            else:
                break

    #Ecuacion de una recta
    elif op == 8:
            # Solicitar las coordenadas del punto
            x1 = float(input("Ingrese la coordenada x del punto: "))
            y1 = float(input("Ingrese la coordenada y del punto: "))

            # Solicitar el valor de la pendiente
            m = float(input("Ingrese el valor de la pendiente: "))

            # Calcular la ecuación de la recta en forma punto-pendiente
            ecuacion = "y - " + str(y1) + " = " + str(m) + "(x - " + str(x1) + ")"

            # Imprimir el resultado
            print("La ecuación de la recta en forma punto-pendiente es:", ecuacion)


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