# De un operario se conoce su sueldo y los años de antigüedad. Se pide
# confeccionar un programa que lea los datos de entrada e informe:
# a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
# b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
# c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

salary = float(input("Por favor, ingrese  el valor del sueldo "))
print("")

old = int(input("Por favor, ingrese los años de antiguedad "))
print("")

if salary < 500 and old >= 10:
    print("Se ha otorgado un aumento del 20%")
    print("El sueldo a pagar es: ", salary * 0.20+salary)

elif salary < 500 and old < 10:
    print("Se ha otorgado un aumento del 5%")
    print("El sueldo a pagar es: ", salary * 0.05+salary)

else:
    if salary >= 500:
        print("El sueldo no requiere cambios")