from suma import Suma
from resta import Resta
from division import Division
from multiplicacion import Multiplicacion
operando_uno = int(input("Ingrese el primer operando: "))
operando_dos = int(input("Ingrese el segundo operando: "))
suma = Suma(operando_uno, operando_dos)
resta = Resta(operando_uno, operando_dos)
division = Division(operando_uno, operando_dos)
multiplicacion = Multiplicacion(operando_uno, operando_dos)
print("El resultado de la suma es: ", suma.sumar())
print("El resultado de la resta es: ", resta.restar())
print("El resultado de la multiplicacion es: ", multiplicacion.multiplicar())
print("El resultado de la division es: ", division.dividir())
