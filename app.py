## 🐍 Código: `gestor_ventas.py`

import csv
import json

# -------------------------------
# Funciones auxiliares
# -------------------------------

def cargar_csv(nombre_archivo):
    datos = []
    try:
        with open(nombre_archivo, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append(fila)
    except FileNotFoundError:
        pass
    return datos

def guardar_csv(nombre_archivo, datos, campos):
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)

def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, mode="w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

# -------------------------------
# Funciones CRUD de productos
# -------------------------------

def registrar_producto(productos):
    id_prod = input("Ingrese ID del producto: ")
    nombre = input("Ingrese nombre: ")
    precio = input("Ingrese precio: ")
    stock = input("Ingrese stock: ")

    producto = {"id": id_prod, "nombre": nombre, "precio": precio, "stock": stock}
    productos.append(producto)
    print("✅ Producto registrado con éxito.")

def consultar_producto(productos):
    id_prod = input("Ingrese ID a consultar: ")
    for prod in productos:
        if prod["id"] == id_prod:
            print(f"📌 Producto encontrado: {prod}")
            return
    print("⚠️ Producto no encontrado.")

def modificar_producto(productos):
    id_prod = input("Ingrese ID a modificar: ")
    for prod in productos:
        if prod["id"] == id_prod:
            prod["nombre"] = input("Nuevo nombre: ")
            prod["precio"] = input("Nuevo precio: ")
            prod["stock"] = input("Nuevo stock: ")
            print("✅ Producto modificado con éxito.")
            return
    print("⚠️ Producto no encontrado.")

def eliminar_producto(productos):
    id_prod = input("Ingrese ID a eliminar: ")
    for prod in productos:
        if prod["id"] == id_prod:
            productos.remove(prod)
            print("🗑️ Producto eliminado con éxito.")
            return
    print("⚠️ Producto no encontrado.")

# -------------------------------
# Funciones de ventas
# -------------------------------

def registrar_venta(productos, ventas):
    id_prod = input("Ingrese ID del producto a vender: ")
    cantidad = int(input("Ingrese cantidad: "))

    for prod in productos:
        if prod["id"] == id_prod:
            if int(prod["stock"]) >= cantidad:
                total = cantidad * float(prod["precio"])
                prod["stock"] = str(int(prod["stock"]) - cantidad)

                venta = {"id_producto": id_prod, "cantidad": cantidad, "total": total}
                ventas.append(venta)
                print(f"✅ Venta registrada. Total: ${total}")
                return
            else:
                print("⚠️ Stock insuficiente.")
                return
    print("⚠️ Producto no encontrado.")

def consultar_ventas(ventas):
    print("\n📊 Historial de ventas:")
    for v in ventas:
        print(v)

# -------------------------------
# Menú principal
# -------------------------------

def menu():
    productos = cargar_csv("productos.csv")
    ventas = cargar_csv("ventas.csv")

    while True:
        print("\n--- Gestor de Ventas ---")
        print("1. Registrar producto")
        print("2. Consultar producto")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Registrar venta")
        print("6. Consultar ventas")
        print("7. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(productos)
        elif opcion == "2":
            consultar_producto(productos)
        elif opcion == "3":
            modificar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            registrar_venta(productos, ventas)
        elif opcion == "6":
            consultar_ventas(ventas)
        elif opcion == "7":
            guardar_csv("productos.csv", productos, ["id", "nombre", "precio", "stock"])
            guardar_csv("ventas.csv", ventas, ["id_producto", "cantidad", "total"])
            guardar_json("productos.json", productos)
            guardar_json("ventas.json", ventas)
            print("💾 Datos guardados en CSV y JSON. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
