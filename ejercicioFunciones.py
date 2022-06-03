import funciones as fn
op = 3

while op != 4:
    print("     MENU    ")
    print("*"*20)
    print("1. Calcular IVA")
    print("2. Descuento")
    print("3. Calcular IMC")
    print("4. Salir")
    op = int(input("Seleccione su opción (1-4): "))
    if op == 1:
        precio = int(input("Ingrese precio del producto: "))
        iva  = fn.calcularIVA(precio)
        print("El IVA de $",precio," es: $",iva)
    if op == 2:
        precio = int(input("Ingrese precio del producto: "))
        desc = int(input("Ingrese descuento (0-100)%: "))
        fn.descuento(precio,desc)
    if op == 3:
        peso = int(input("Ingrese su peso en Kg: "))
        estatura = float(input("Ingrese su estatura en m: "))
        fn.calculoIMC(peso,estatura)

print("Fin del semestre")
print("FIN")
