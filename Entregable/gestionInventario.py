def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")

def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    # Verificar si el producto ya existe
    if nombre in inventario:
        print(f"¡El producto '{nombre}' ya existe en el inventario!")
        opcion = input("¿Desea actualizar la cantidad? (s/n): ").lower()
        if opcion != 's':
            return
    
    # Solicitar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")
    
    inventario[nombre] = cantidad
    print(f"Producto '{nombre}' agregado/actualizado con éxito.")

def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado con éxito.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    
    print("\n--- Inventario Actual ---")
    print("{:<20} {:<10}".format("Producto", "Cantidad"))
    print("-" * 30)
    for producto, cantidad in inventario.items():
        print("{:<20} {:<10}".format(producto, cantidad))

def main():
    inventario = {}
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            eliminar_producto(inventario)
        elif opcion == '3':
            mostrar_inventario(inventario)
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()