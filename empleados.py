import json
empleados = [
    {"id": 1, "nombre": "Juan", "salario": 50000},
    {"id": 2, "nombre": "Ana", "salario": 55000},
    {"id": 3, "nombre": "Carlos", "salario": 60000},
    {"id": 4, "nombre": "Marta", "salario": 52000},
    {"id": 5, "nombre": "Luis", "salario": 58000}
]
with open("empleados.txt", "w") as archivo:
    for empleado in empleados:
        archivo.write(json.dumps(empleado) + "\n")
empleados_cargados = []
with open("empleados.txt", "r") as archivo:
    for linea in archivo:
        empleados_cargados.append(json.loads(linea.strip()))
id_modificar = int(input("Ingrese el ID del empleado cuyo salario quiera modificar:"))
nuevo_salario = float(input("Ingrese el nuevo salario:"))
encontrado = False
for empleado in empleados_cargados:
    if empleado["id"] == id_modificar:
        empleado["salario"] = nuevo_salario
        encontrado = True
        break
if not encontrado:
    print("Error: El ID ingresado no existe.")
else:
    with open("empleados.txt", "w") as archivo:
        for empleado in empleados_cargados:
            archivo.write(json.dumps(empleado) + "\n")
    print("Lista de empleados actualizada:")
    for empleado in empleados_cargados:
        print(empleado)