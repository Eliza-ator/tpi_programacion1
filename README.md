# tpi_programacion1
Trabajo Prá# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1**
Tecnicatura Universitaria en Programación | UTN — TUP a Distancia

---

## Descripción

Aplicación de consola en Python que permite gestionar un dataset de países.
Lee los datos desde un archivo CSV y ofrece un menú interactivo con las siguientes funcionalidades:

- Agregar y actualizar países
- Buscar por nombre (coincidencia parcial)
- Filtrar por continente, rango de población o rango de superficie
- Ordenar por nombre, población o superficie (ascendente o descendente)
- Ver estadísticas: máximos, mínimos, promedios y conteo por continente

---

## Estructura del proyecto

```
TPI_Paises/
├── main.py        # Programa principal
├── paises.csv     # Dataset base con 24 países
└── README.md      # Este archivo
```

---

## Requisitos

- Python 3.x (sin bibliotecas externas)

---

## Cómo ejecutar

```bash
python main.py
```

El programa carga automáticamente `paises.csv` desde la misma carpeta.

---

## Formato del CSV

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

Campos obligatorios: `nombre` (str), `poblacion` (int), `superficie` (int), `continente` (str).
Continentes válidos: `América`, `Europa`, `Asia`, `África`, `Oceanía`.

---

## Ejemplo de uso

```
GESTIÓN DE DATOS DE PAÍSES  —  MENÚ
===============================================
  1. Mostrar todos los países
  2. Agregar un país
  3. Actualizar un país
  4. Buscar país por nombre
  5. Filtrar por continente
  6. Filtrar por rango de población
  7. Filtrar por rango de superficie
  8. Ordenar países
  9. Ver estadísticas
  0. Salir
```

**Buscar por nombre parcial:**
```
Ingresá el nombre o parte del nombre: br
Resultados para 'br' (1 encontrado/s):
  Brasil         213,993,437    8,515,767  América
```

**Estadísticas:**
```
  POBLACIÓN
  Mayor : China (1,412,600,000)
  Menor : Nueva Zelanda (5,084,300)
  Prom. : 164,936,587 habitantes

  PAÍSES POR CONTINENTE
  América    :  6  ██████
  Europa     :  6  ██████
  Asia       :  7  ███████
  África     :  5  █████
  Oceanía    :  2  ██
```

---

## Integrantes

| Nombre | Legajo / DNI |
|--------|-------------|
| Ator, Elizabeth | _______________ |

---

## Links

- 📄 Documentación PDF: 
- 🎥 Video demostrativo: 

