#By Zahid Martínez
c1 = float(input("Ingrese la calificación del primer parcial: "))
c2 = float(input("Ingrese la calificación del segundo parcial: "))
c3 = float(input("Ingrese la calificación del tercer parcial: "))
prom = (c1 + c2 + c3)/ 3
if prom >= 70:
  print("Ha aprobado con un promedio de: ", prom )
else:
  print("Ha reprobado con un promedio de: ", prom )	