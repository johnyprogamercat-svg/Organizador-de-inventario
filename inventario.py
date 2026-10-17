import time
Lista_productos = []
nombre_agregado = ""
precio_agregado = ""
cantidad_agregada = ""
categoria_agregada = ""


def agregar_producto():
    nombre_agregado = input("Nombre del producto: ")
    precio_agregado = float(input("Precio del producto: "))
    cantidad_agregada = float(input("Cantidad del producto: "))
    categoria_agregada = input("Categoria del producto: ")

    Producto = {"nombre": nombre_agregado,
     "precio": precio_agregado,
     "cantidad": cantidad_agregada,
     "categoria": categoria_agregada}
    Lista_productos.append(Producto)


def mostrar_estado():
    if not Lista_productos:
        print("La lista está vacía")
    else:
        for Producto in Lista_productos:
            print(Producto["nombre"], Producto["precio"], Producto["cantidad"], Producto["categoria"])
    print(Lista_productos)
    return Lista_productos

def buscar_producto(nombre):
    for Producto in Lista_productos:
        if Producto["nombre"] == nombre:
            print(Producto["nombre"], Producto["precio"], Producto["cantidad"], Producto["categoria"])

def actualizar_stock(nombre, nueva_cantidad):
    for Producto in Lista_productos:
        if nombre == Producto["nombre"]:
            Producto["cantidad"] = nueva_cantidad

print("Bienvenido al supermarket manager, ver 1.0")
time.sleep(1)
while True:
    Decision = int(input("¿Qué deseas hacer? Agregar producto: 1 | Mostrar estado actual: 2 | Buscar un producto: 3 | Actualizar stock de un producto: 4 | Salir: 5 | = "))
    if Decision == 1:
        agregar_producto()
    if Decision == 2:
        mostrar_estado()
    if Decision == 3:
        nombre = input("Ingresa el nombre del producto: ")
        buscar_producto(nombre)
    if Decision == 4:
        nombre = input("Ingrese el nombre del producto: ")
        nueva_cantidad = int(input("Ingrese la cantidad actualizada"))
        actualizar_stock(nombre, nueva_cantidad)
    if Decision == 5:
        break
