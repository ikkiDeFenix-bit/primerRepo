#EJEMPLO DE CARRITO DE COMPRAS

archivo_carrito = 'carrito_compras.txt'
carrito = []

try:
    with open(archivo_carrito, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            linea.strip() #elimina cualquier espacio en blanco que exista en cada una de las lineas
            if linea.startswith("- "):
                producto =linea[2:] #evitamos el '-' y el ' '
                carrito.append(producto)
        print("Carrito cargado desde el archivo")
except FileNotFoundError:
    print("No existe el archivo, iniciando carrito vacio...")


#MENU PRINCIPAL
print("\n CARRITO DE COMPRAS")
print("Opciones: ")
print("1 .- Agregar productos")
print("2 .- Quitar productos")
print("3 .- Mostrar productos")
print("4 .- Salir y guardar")
print("==============\n")

while True:
    opcion = input("Elige una opcion (1-4): ")

    if opcion == '1':
        producto = input("Nombre del producto a agregar: ")
        carrito.append(producto)
        print(f"-> {producto} agregado al carrito \n")
    elif opcion == '2':
        producto = input("Nombre del producto a eliminar: ")
        if producto in carrito:
            carrito.remove(producto)
        else:
            print("Este producto no está en el carrito\n")
        print(f"-> {producto} eliminado del carrito \n")
    elif opcion == '3':
        print(f"\n=======CARRITO ACTUAL")
        if(len(carrito)==0):
            print("El carrito está vacío")
        else:
            for item in carrito:
                print(f" - {item}")
            print("\n")
    elif opcion == '4':
        with open(archivo_carrito, 'w') as archivo:
            if len(carrito)==0:
                archivo.write("CARRITO VACÍO \n")
            else:
                for item in carrito:
                    archivo.write(f"- {item}\n")
        break
    elif opcion == '5':
        productoEditar=input("Ingrese el nombre del producto a editar : ")
        if productoEditar in carrito:
            indice = carrito.index(productoEditar)
            nuevoProducto = input("Ingrese el nombre modificado : ")
            carrito[indice] = nuevoProducto
            print("Producto modificado")
        else:
            print("Producto no existe en la lista\n")
    else:
        print("Opcion no válida, intente otra vez")
print("Se ha finalizado el programa guardando el carrito")
print("Hola, nuevo commit")
listaEjemplo = [1,2,3,4,5]
for elemento in listaEjemplo:
    print("El numero es :")
    print(elemento)

print("Nuevo cambio")
print("Cambio 2")
print("Cambio 3")

print("Cambio 4")

print("Cambio 5")

print("Este es un nuevo cambio desarrollado en nube")
