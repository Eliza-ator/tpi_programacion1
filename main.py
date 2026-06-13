# main.py — Punto de entrada del programa
# TPI - Gestión de Datos de Países en Python


from config import ARCHIVO_CSV
from modulo_csv import leer_csv
from modulo_crud import mostrar_paises, agregar_pais, actualizar_pais
from modulo_filtros import buscar_por_nombre, filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from modulo_orden_estadisticas import ordenar_paises, mostrar_estadisticas


def mostrar_menu():
    """Imprime el menú principal de opciones en consola."""
    print("\n" + "="*47)
    print("    GESTIÓN DE DATOS DE PAÍSES  —  MENÚ")
    print("="*47)
    print("  1. Mostrar todos los países")
    print("  2. Agregar un país")
    print("  3. Actualizar un país")
    print("  4. Buscar país por nombre")
    print("-"*47)
    print("  5. Filtrar por continente")
    print("  6. Filtrar por rango de población")
    print("  7. Filtrar por rango de superficie")
    print("-"*47)
    print("  8. Ordenar países")
    print("  9. Ver estadísticas")
    print("-"*47)
    print("  0. Salir")
    print("="*47)


def main():
    """Función principal: carga el dataset y ejecuta el bucle del menú.

    Lee los datos desde el CSV al iniciar. Si el archivo no existe,
    informa al usuario y termina el programa. Mientras el usuario no
    elija salir (opción 0), sigue mostrando el menú y despachando
    la opción elegida a la función correspondiente.
    """
    print("="*47)
    print("  Gestión de Datos de Países — UTN TUP")
    print("="*47)
    print("Cargando datos desde el CSV...")

    paises = leer_csv(ARCHIVO_CSV)

    if paises is None:
        print(f"No se pudo cargar '{ARCHIVO_CSV}'. Verificá que el archivo exista.")
        return

    print(f"{len(paises)} países cargados correctamente.\n")

    while True:
        mostrar_menu()
        opcion = input("  Ingresá una opción: ").strip()

        if   opcion == "1": mostrar_paises(paises)
        elif opcion == "2": agregar_pais(paises)
        elif opcion == "3": actualizar_pais(paises)
        elif opcion == "4": buscar_por_nombre(paises)
        elif opcion == "5": filtrar_por_continente(paises)
        elif opcion == "6": filtrar_por_poblacion(paises)
        elif opcion == "7": filtrar_por_superficie(paises)
        elif opcion == "8": ordenar_paises(paises)
        elif opcion == "9": mostrar_estadisticas(paises)
        elif opcion == "0":
            print("\n¡Gracias, vuelva pronto!")
            break
        else:
            print("Eroro: opción incorrecta. Ingresá un número del 0 al 9.")


if __name__ == "__main__":
    main()
