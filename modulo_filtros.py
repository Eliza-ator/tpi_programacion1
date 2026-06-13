# modulo_filtros.py — Búsqueda y filtros de países
# TPI - Gestión de Datos de Países en Python


from config import CONTINENTES_VALID
from modulo_crud import mostrar_paises, pedir_entero


def buscar_por_nombre(paises):
    """Busca países cuyo nombre contenga el texto ingresado.

    La búsqueda es parcial y no distingue mayúsculas de minúsculas.
    Ejemplo: escribir 'ar' encuentra Argentina y Arabia Saudita.
    Si no hay resultados, informa al usuario.
    """
    print("\n--- BUSCAR POR NOMBRE ---")

    if not paises:
        print("No hay países cargados.")
        return

    texto = input("Nombre o parte del nombre a buscar: ").strip()
    if not texto:
        print("El texto de búsqueda no puede estar vacío.")
        return

    resultados = [p for p in paises if texto.lower() in p["nombre"].lower()]

    if not resultados:
        print(f"\No se encontraron países con '{texto}'.")
        return

    print(f"\nResultados para '{texto}' ({len(resultados)} encontrado/s):")
    mostrar_paises(resultados)


def filtrar_por_continente(paises):
    """Muestra todos los países que pertenecen al continente indicado.

    Valida que el continente sea uno de los 5 reconocidos por el sistema.
    La comparación no distingue mayúsculas de minúsculas.
    Presionando Enter sin escribir nada se cancela la operación.
    """
    print("\n--- FILTRAR POR CONTINENTE ---")

    if not paises:
        print("No hay países cargados.")
        return

    print("Continentes disponibles:", ", ".join(CONTINENTES_VALID))
    print("(Presioná Enter sin escribir nada para cancelar)")
    while True:
        continente = input("Continente: ").strip()
        if not continente:
            print("Operación cancelada.")
            return
        encontrado = next((c for c in CONTINENTES_VALID if c.lower() == continente.lower()), None)
        if not encontrado:
            print(f"Continente no reconocido. Opciones: {', '.join(CONTINENTES_VALID)}")
            continue
        continente = encontrado
        break

    resultados = [p for p in paises if p["continente"] == continente]

    if not resultados:
        print(f"\nNo se encontraron países en '{continente}'.")
        return

    print(f"\nPaíses en {continente} ({len(resultados)} encontrado/s):")
    mostrar_paises(resultados)


def filtrar_por_rango(paises, campo):
    """Filtra países dentro de un rango numérico para el campo indicado.

    Parámetros:
      paises : lista de diccionarios con los datos de países
      campo  : "poblacion" o "superficie"

    Pide mínimo y máximo, valida que el mínimo no supere al máximo,
    y muestra los países dentro del rango.
    """
    etiqueta = "población" if campo == "poblacion" else "superficie en km²"

    minimo = pedir_entero(f"{etiqueta.capitalize()} mínima: ", minimo=0)

    while True:
        maximo = pedir_entero(f"{etiqueta.capitalize()} máxima: ", minimo=0)
        if maximo < minimo:
            print(f"El máximo ({maximo:,}) no puede ser menor que el mínimo ({minimo:,}).")
            continue
        break

    resultados = [p for p in paises if minimo <= p[campo] <= maximo]

    if not resultados:
        print(f"\nNo hay países con {etiqueta} entre {minimo:,} y {maximo:,}.")
        return

    print(f"\nPaíses con {etiqueta} entre {minimo:,} y {maximo:,} ({len(resultados)} encontrado/s):")
    mostrar_paises(resultados)


def filtrar_por_poblacion(paises):
    """Filtra países dentro de un rango de población ingresado por el usuario."""
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")
    if not paises:
        print("No hay países cargados.")
        return
    filtrar_por_rango(paises, "poblacion")


def filtrar_por_superficie(paises):
    """Filtra países dentro de un rango de superficie ingresado por el usuario."""
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")
    if not paises:
        print("No hay países cargados.")
        return
    filtrar_por_rango(paises, "superficie")
