# ============================================================
# modulo_crud.py — Operaciones CRUD sobre países
# TPI - Gestión de Datos de Países en Python
# Tecnicatura Universitaria en Programación - UTN
# ============================================================

from config import ARCHIVO_CSV, CONTINENTES_VALID
from modulo_csv import guardar_csv


def pedir_entero(mensaje, minimo=1, permitir_vacio=False, valor_actual=None):
    """Solicita al usuario un número entero y valida la entrada.

    Parámetros:
      mensaje        : texto que se muestra al usuario
      minimo         : valor mínimo aceptado (por defecto 1)
      permitir_vacio : si True, Enter devuelve valor_actual sin cambios
      valor_actual   : valor que se conserva cuando el usuario presiona Enter

    Retorna el entero ingresado, o valor_actual si se permitió vacío y
    el usuario presionó Enter.
    """
    while True:
        entrada = input(mensaje).strip()

        if permitir_vacio and entrada == "":
            return valor_actual

        if entrada == "":
            print("⚠ Este campo no puede estar vacío.")
            continue

        try:
            numero = int(entrada)
            if numero < minimo:
                print(f"⚠ El valor debe ser mayor o igual a {minimo}.")
                continue
            return numero
        except ValueError:
            print("⚠ Ingresá un número entero válido (sin letras ni símbolos).")


def mostrar_paises(paises):
    """Muestra la lista de países en formato de tabla con columnas alineadas.

    Si la lista está vacía, informa al usuario.
    Los números se muestran con separador de miles para mejor legibilidad.
    """
    if not paises:
        print("\n⚠ No hay países para mostrar.")
        return

    print("\n" + "="*65)
    print(f"  {'PAÍS':<20} {'POBLACIÓN':>14} {'SUPERFICIE km²':>14} {'CONTINENTE'}")
    print("-"*65)
    for pais in paises:
        print(
            f"  {pais['nombre']:<20}"
            f"{pais['poblacion']:>14,}"
            f"{pais['superficie']:>14,}"
            f"  {pais['continente']}"
        )
    print("="*65)
    print(f"  Total: {len(paises)} país/es")


def agregar_pais(paises):
    """Solicita los datos al usuario y agrega un nuevo país a la lista.

    Reglas:
    - Ningún campo puede estar vacío.
    - Población y superficie deben ser enteros positivos.
    - No se puede agregar un país cuyo nombre ya exista (sin distinción
      de mayúsculas/minúsculas).
    - Al finalizar guarda los cambios en el CSV.
    """
    print("\n--- AGREGAR PAÍS ---")

    # --- Nombre ---
    while True:
        nombre = input("Nombre del país: ").strip()
        if not nombre:
            print("⚠ El nombre no puede estar vacío.")
            continue
        if any(p["nombre"].lower() == nombre.lower() for p in paises):
            print(f"⚠ El país '{nombre}' ya existe en el sistema.")
            return
        break

    # --- Población y Superficie usando la función auxiliar ---
    poblacion  = pedir_entero("Población (número entero positivo): ")
    superficie = pedir_entero("Superficie en km² (número entero positivo): ")

    # --- Continente ---
    print("Continentes disponibles:", ", ".join(CONTINENTES_VALID))
    while True:
        continente = input("Continente: ").strip()
        if not continente:
            print("⚠ El continente no puede estar vacío.")
            continue
        encontrado = next((c for c in CONTINENTES_VALID if c.lower() == continente.lower()), None)
        if not encontrado:
            print(f"⚠ Continente no reconocido. Opciones: {', '.join(CONTINENTES_VALID)}")
            continue
        continente = encontrado
        break

    # --- Crear diccionario y guardar ---
    nuevo_pais = {
        "nombre":     nombre,
        "poblacion":  poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)

    if guardar_csv(ARCHIVO_CSV, paises):
        print(f"\n✔ País '{nombre}' agregado y guardado correctamente.")
    else:
        print("⚠ País agregado en memoria pero no se pudo guardar en el archivo.")


def actualizar_pais(paises):
    """Actualiza población y/o superficie de un país existente.

    Busca el país por nombre exacto (sin distinción de mayúsculas).
    Si el usuario presiona Enter en un campo, conserva el valor actual.
    Guarda los cambios en el CSV al finalizar.
    """
    print("\n--- ACTUALIZAR PAÍS ---")

    if not paises:
        print("⚠ No hay países cargados.")
        return

    nombre = input("Nombre del país a actualizar: ").strip()
    if not nombre:
        print("⚠ El nombre no puede estar vacío.")
        return

    pais_encontrado = next(
        (p for p in paises if p["nombre"].lower() == nombre.lower()), None
    )

    if pais_encontrado is None:
        print(f"⚠ No se encontró el país '{nombre}'.")
        return

    print(f"\nDatos actuales de {pais_encontrado['nombre']}:")
    print(f"  Población : {pais_encontrado['poblacion']:,}")
    print(f"  Superficie: {pais_encontrado['superficie']:,} km²")
    print("(Presioná Enter para conservar el valor actual)")

    pais_encontrado["poblacion"] = pedir_entero(
        f"\nNueva población [{pais_encontrado['poblacion']:,}]: ",
        permitir_vacio=True,
        valor_actual=pais_encontrado["poblacion"]
    )
    pais_encontrado["superficie"] = pedir_entero(
        f"Nueva superficie km² [{pais_encontrado['superficie']:,}]: ",
        permitir_vacio=True,
        valor_actual=pais_encontrado["superficie"]
    )

    if guardar_csv(ARCHIVO_CSV, paises):
        print(f"\n✔ País '{pais_encontrado['nombre']}' actualizado correctamente.")
    else:
        print("⚠ Cambios aplicados en memoria pero no se pudo guardar en el archivo.")
