# Ejercicio Integrador - FastAPI

Ejercicio integrador realizado para practicar la creación de una API REST utilizando FastAPI.

## Estructura

La aplicación está organizada en módulos para trabajar con:

- Categorías
- Productos

Cada módulo separa las rutas, los esquemas de datos y la lógica de la aplicación.

## Ejecutar el proyecto

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la API:

```bash
python -m fastapi dev app/main.py
```

La documentación de la API se puede consultar en `/docs`.

## Endpoints

La API permite:

- Crear categorías
- Listar categorías
- Buscar una categoría por id
- Crear productos
- Listar productos
- Buscar un producto por id