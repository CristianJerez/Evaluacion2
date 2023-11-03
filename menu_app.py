def agregar_compra(lista_compras):
    nombre_compra = input("Ingrese el nombre de su compra: ")
    precio_compra = float(input("Ingrese el precio de la compra: "))
    lista_compras[nombre_compra]=precio_compra
    print("Nueva compra agregada correctamente.")

def mostrar_compras(lista_compras):
    if lista_compras == 0:
        return print("No hay compras registradas.")
    else:
        for idx, nombre_compra in enumerate(lista_compras, start=1):
            print(f"{idx}.Producto: {nombre_compra} Precio: ${lista_compras[nombre_compra]:,.2f}")

def mostrar_total(lista_compras):
    totalGasto = sum(lista_compras.values())
    return print(f"El total gastado es: ${totalGasto:,.2f}")

def main():
    compras = {}
    total_gastado = 0
    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion = input("Favor, seleccione una opción: ")

        if opcion == "1":
            agregar_compra(compras)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
                mostrar_total(compras)
        elif opcion == "4":
            print("A salido del programa. Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
main()