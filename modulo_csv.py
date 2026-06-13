# ============================================================
# modulo_csv.py — Lectura y escritura del archivo CSV
# TPI - Gestión de Datos de Países en Python
# Tecnicatura Universitaria en Programación - UTN
# ============================================================


def leer_csv(ruta):
    """Lee el archivo CSV y devuelve una lista de diccionarios.

    Cada fila válida se convierte en un diccionario con claves:
      nombre (str), poblacion (int), superficie (int), continente (str)

    Las filas con formato incorrecto se informan y se ignoran.
    Retorna None si el archivo no existe.
    Retorna lista vacía si el archivo no tiene datos válidos.
    """
    paises = []
    try:
        archivo = open(ruta, "r", encoding="utf-8")
        lineas  = archivo.readlines()
        archivo.close()

        if len(lineas) < 2:
            print("⚠ El archivo CSV está vacío o solo tiene encabezado.")
            return paises

        # Salteamos la primera línea (encabezado)
        for numero, linea in enumerate(lineas[1:], start=2):
            linea = linea.strip()
            if linea == "":
                continue  # Ignoramos líneas en blanco

            partes = linea.split(",")

            # Validamos que tenga exactamente 4 campos
            if len(partes) != 4:
                print(f"⚠ Línea {numero} ignorada (se esperaban 4 campos): {linea}")
                continue

            nombre     = partes[0].strip()
            continente = partes[3].strip()

            # Validamos que población y superficie sean enteros
            try:
                poblacion  = int(partes[1].strip())
                superficie = int(partes[2].strip())
            except ValueError:
                print(f"⚠ Línea {numero} ignorada (población/superficie no son números): {linea}")
                continue

            # Validamos que no haya campos de texto vacíos
            if not nombre or not continente:
                print(f"⚠ Línea {numero} ignorada (campos vacíos): {linea}")
                continue

            # Validamos que los números sean positivos
            if poblacion <= 0 or superficie <= 0:
                print(f"⚠ Línea {numero} ignorada (población/superficie deben ser positivos): {linea}")
                continue

            pais = {
                "nombre":     nombre,
                "poblacion":  poblacion,
                "superficie": superficie,
                "continente": continente
            }
            paises.append(pais)

    except FileNotFoundError:
        print(f"✖ No se encontró el archivo '{ruta}'.")
        return None

    return paises


def guardar_csv(ruta, paises):
    """Guarda la lista de países en el archivo CSV.

    Sobreescribe el archivo con los datos actuales incluyendo el encabezado.
    Retorna True si tuvo éxito, False en caso de error.
    """
    try:
        archivo = open(ruta, "w", encoding="utf-8")
        archivo.write("nombre,poblacion,superficie,continente\n")  # Encabezado
        for pais in paises:
            linea = (f"{pais['nombre']},"
                     f"{pais['poblacion']},"
                     f"{pais['superficie']},"
                     f"{pais['continente']}\n")
            archivo.write(linea)
        archivo.close()
        return True
    except Exception as e:
        print(f"✖ Error al guardar el archivo: {e}")
        return False
