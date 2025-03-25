# 1. Resta 100 

ingreso = int(input("ingrese su edad: "))
print(f"te faltan  {100 - ingreso} para los 100 años")

# 2. C -> F

tempC = float(input("ingrese temperatura: "))
tempF = tempC*9/5+32
print(f"{tempC}ºC equivalen a {tempF}ºF")

# 3. Suma 100

sum = 0
for i in range(1,101):
    sum += i
print(f"la suma de los primeros 100 numeros naturales es {sum}")

# 4. Encuentra pares

ArregloNum = [1,2,5,3,76,4,6,974,12,58,1,6745,123,865,124,674,23,568,238,2,23,9]
for num in ArregloNum:
    if not(num%2):
        print(f"{num} es par")

# 5. Ingreso e impresión hasta negativo

arregloNums = input("inglese numeros separados por un espacio: ").split(" ")
for num in arregloNums:
    if (int(num) < 0):
        print(f"se ha encontrado un numero negativo: {num}")
        break
    print(f"{num}")

# 4. Encuentra pares, division en lista de impar y par
listaPar = []
listaImpar = []
ArregloNum = [1,2,5,3,76,4,6,974,12,58,1,6745,123,865,124,674,23,568,238,2,23,9]
for num in ArregloNum:
    if not(num%2):
        listaPar.append(num)
    else:
        listaImpar.append(num)

print(f"Impares: {listaImpar}\nPares: {listaPar}")
