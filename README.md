# Liga BetPlay (Consola en Python)

Proyecto base en Python para gestionar información de una liga de fútbol (equipos, y futuras funcionalidades como jugadores, fechas y estadísticas) desde una interfaz de consola.

## Descripción general

La aplicación inicia en `main.py` y delega el flujo al menú principal en `modules/ui/mainMenu.py`.
Actualmente, la opción implementada del menú es **Agregar Equipo** (a través de `modules/teams/team.py`).

El proyecto también incluye un módulo de utilidades para pantalla (`modules/utils.py`) y un módulo de persistencia JSON (`modules/corefiles.py`).

## Estructura del proyecto

```text
ligaBetPlay/
├── main.py
├── data/
│   ├── ligabetplay.json
│   └── teams.json
└── modules/
    ├── corefiles.py
    ├── utils.py
    ├── teams/
    │   └── team.py
    └── ui/
        └── mainMenu.py
```

## Flujo de ejecución

1. `main.py` crea el diccionario `ligaBetPlay`.
2. Llama a `menu.menuOptions(ligaBetPlay)`.
3. `menuOptions` muestra el menú y despacha según la opción elegida.

## Requisitos

- Python 3.10+ (se usa `match/case` en el menú).
- Sistema operativo Windows/Linux/macOS.

## Ejecución

Desde la raíz del proyecto:

```bash
python main.py
```

## Módulo `modules/corefiles.py`

Este archivo centraliza operaciones de lectura/escritura de archivos JSON en la carpeta `data/`.

- Constante `BASE_URL = 'data/'`
  - Define la ruta base donde se buscan y guardan archivos de datos.

### Funciones

- `checkFile(archivo: str, data)`
  - Verifica si existe `data/<archivo>`.
  - Si no existe, crea el archivo y escribe `data` como JSON inicial.
  - Uso típico: asegurar estructura de datos al iniciar.

- `readDataFile(archivo) -> dict`
  - Abre `data/<archivo>` en modo lectura/escritura (`r+`) y retorna el contenido parseado con `json.load`.
  - Espera que el archivo exista y tenga JSON válido.

- `createData(archivo, data)`
  - Crea/sobrescribe `data/<archivo>` en modo `w+`.
  - Guarda `data` serializado con indentación.

- `updateData(data, srcData)`
  - Función interactiva para modificar campos de un proveedor (`data`) preguntando por consola qué propiedades editar.
  - Recorre claves del diccionario y solicita nuevos valores (excepto `nit`).
  - Al final actualiza `srcData['proveedores']` y persiste en `inventario.json` usando `UpdateFile`.
  - Si `data` está vacío, muestra mensaje de no encontrado.

- `UpdateFile(archivo, data)`
  - Sobrescribe `data/<archivo>` con el diccionario `data` en formato JSON.
  - Es el método de persistencia general utilizado por otras funciones.

- `delData(data)`
  - Solicita por consola el `nit` de un proveedor.
  - Elimina la entrada correspondiente de `data['proveedores']`.
  - Persiste cambios en `inventario.json` con `UpdateFile`.

- `searchProv(data)`
  - Solicita por consola el `nit` a buscar en `data['proveedores']`.
  - Obtiene y desestructura el proveedor encontrado (incluyendo dirección).
  - Actualmente solo imprime `Nit {nit}:` y pausa la pantalla.

## Observaciones técnicas sobre `corefiles.py`

- El módulo mezcla utilidades genéricas de JSON con lógica específica de **proveedores/inventario** (`inventario.json`, claves `proveedores`, `nit`).
- Varias funciones (`updateData`, `delData`, `searchProv`) dependen de estructura de datos específica y entrada interactiva por consola.
- Hay uso de `os.system('cls')` y `os.system('pause')`, orientado principalmente a Windows.

## Próximas mejoras sugeridas

1. Separar persistencia genérica (CRUD JSON) de lógica de dominio (proveedores/equipos).
2. Manejar errores cuando el `nit` no existe antes de usar `.pop()` o `.values()`.
3. Estandarizar utilidades de consola usando `modules/utils.py` para mantener compatibilidad multiplataforma.
