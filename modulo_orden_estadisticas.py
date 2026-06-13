# ============================================================
# modulo_orden_estadisticas.py — Ordenamientos y estadísticas
# TPI - Gestión de Datos de Países en Python
# Tecnicatura Universitaria en Programación - UTN
# ============================================================

from modulo_crud import mostrar_paises


def ordenar_paises(paises):
    """Ordena países por nombre, población o superficie (ascendente o descendente).

    Implementa el algoritmo Bubble Sort (burbuja) de forma manual.
    Trabaja sobre una copia de la lista para no modificar el dataset original.
    El resultado se muestra en pantalla.
    """
    print("\n--- ORDENAR PAÍSES ---")

    if not paises:
        print("⚠ No hay países cargados.")
        return

    # --- Criterio ---
    print("Ordenar por:  1. Nombre   2. Población   3. Superficie")
    while True:
        criterio = input("Elegí una opción (1-3): ").strip()
        if criterio in ("1", "2", "3"):
            break
        print("⚠ Opción inválida. Ingresá 1, 2 o 3.")

    # --- Dirección ---
    print("Dirección:    1. Ascendente (A→Z / menor→mayor)   2. Descendente (Z→A / mayor→menor)")
    while True:
        direccion = input("Elegí una opción (1-2): ").strip()
        if direccion in ("1", "2"):
            break
        print("⚠ Opción inválida. Ingresá 1 o 2.")

    invertir = (direccion == "2")

    opciones = {"1": ("nombre", "Nombre"), "2": ("poblacion", "Población"), "3": ("superficie", "Superficie")}
    clave, nombre_crit = opciones[criterio]

    # --- Bubble Sort sobre una copia ---
    resultado = list(paises)  # Copia para no alterar la lista original
    n = len(resultado)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            val_a = resultado[j][clave]
            val_b = resultado[j + 1][clave]

            # Comparación sin distinción de mayúsculas para strings
            if isinstance(val_a, str):
                val_a = val_a.lower()
                val_b = val_b.lower()

            # Intercambiamos si el orden no coincide con la dirección elegida
            if (not invertir and val_a > val_b) or (invertir and val_a < val_b):
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]

    direccion_txt = "descendente" if invertir else "ascendente"
    print(f"\nPaíses ordenados por {nombre_crit} ({direccion_txt}):")
    mostrar_paises(resultado)


def mostrar_estadisticas(paises):
    """Muestra estadísticas generales del dataset.

    Calcula y muestra:
    - País con mayor y menor población (búsqueda manual del máx/mín)
    - País con mayor y menor superficie (búsqueda manual del máx/mín)
    - Promedio de población (suma manual dividida por total)
    - Promedio de superficie (suma manual dividida por total)
    - Cantidad de países por continente (con barra visual)
    """
    print("\n--- ESTADÍSTICAS ---")

    if not paises:
        print("⚠ No hay países cargados.")
        return

    total = len(paises)

    # --- Mayor y menor población: recorrido manual ---
    pais_mayor_pob = paises[0]
    pais_menor_pob = paises[0]
    for pais in paises[1:]:
        if pais["poblacion"] > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = pais
        if pais["poblacion"] < pais_menor_pob["poblacion"]:
            pais_menor_pob = pais

    # --- Mayor y menor superficie: recorrido manual ---
    pais_mayor_sup = paises[0]
    pais_menor_sup = paises[0]
    for pais in paises[1:]:
        if pais["superficie"] > pais_mayor_sup["superficie"]:
            pais_mayor_sup = pais
        if pais["superficie"] < pais_menor_sup["superficie"]:
            pais_menor_sup = pais

    # --- Promedios: suma manual dividida por total ---
    suma_pob = 0
    suma_sup = 0
    for pais in paises:
        suma_pob += pais["poblacion"]
        suma_sup += pais["superficie"]
    prom_pob = suma_pob // total  # División entera para obtener entero
    prom_sup = suma_sup // total

    # --- Cantidad por continente: diccionario como contador ---
    por_continente = {}
    for pais in paises:
        c = pais["continente"]
        if c in por_continente:
            por_continente[c] += 1
        else:
            por_continente[c] = 1

    # --- Mostrar resultados ---
    print("\n" + "="*55)
    print("  POBLACIÓN")
    print("-"*55)
    print(f"  Mayor : {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,})")
    print(f"  Menor : {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,})")
    print(f"  Prom. : {prom_pob:,} habitantes")
    print("\n  SUPERFICIE")
    print("-"*55)
    print(f"  Mayor : {pais_mayor_sup['nombre']} ({pais_mayor_sup['superficie']:,} km²)")
    print(f"  Menor : {pais_menor_sup['nombre']} ({pais_menor_sup['superficie']:,} km²)")
    print(f"  Prom. : {prom_sup:,} km²")
    print("\n  PAÍSES POR CONTINENTE")
    print("-"*55)
    for continente, cantidad in por_continente.items():
        barra = "█" * cantidad
        print(f"  {continente:<12}: {cantidad:>2}  {barra}")
    print("="*55)
    print(f"  Total de países en el sistema: {total}")
