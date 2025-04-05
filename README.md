# QR Code Generator API

Una API REST desarrollada con FastAPI para generar códigos QR con estilo personalizado.

## Descripción

Esta API permite generar códigos QR para el sistema de Activo Fijo, con las siguientes características:
- Generación de QR con esquinas redondeadas
- Alta corrección de errores
- Formato de salida PNG
- Integración con el sistema de Activo Fijo

## Requisitos

- Python 3.13 o superior
- FastAPI
- qrcode[pil]

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/qrAPI.git
 ```

2. Instalar dependencias usando uv (recomendado) o pip:
```bash
uv pip install -r requirements.txt
or

uv sync
 ```

## Uso
1. Iniciar el servidor:
```bash
uvicorn main:app --reload
 ```

2. La API estará disponible en http://localhost:8000
### Endpoints Disponibles Ruta Principal
```plaintext
GET /
Response: {"Hello": "World"}
 ```
 Generar QR para Activo Fijo
```plaintext
GET /qrActivoFijo/
Response: Imagen PNG del código QR
 ```

Ejemplo de uso:

```plaintext
GET /qrActivoFijo
body
{
    "data": "https://example.com/https://example.com/12345",
    "logoURL": "",
    "back_color": "#232B99",
    "edge_color": "#FFF200",
    "center_color": "#FFF200",
    "selected_drawer": "square",
    "ratio": 0.3
}
 ```

Generará un código QR que enlaza a: https://example.com/12345

## Características Técnicas
- Framework: FastAPI
- Generación de QR: qrcode
- Estilo: Multiples Modulos
- Formato de salida: PNG
- Error Correction Level: H (Alto)
- Tamaño de módulo: 10
- Borde: 4 módulos
## Documentación API
FastAPI genera automáticamente la documentación de la API. Puedes acceder a:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
## Desarrollo
El proyecto utiliza:

- FastAPI para el framework web
- qrcode para la generación de códigos QR
- Pillow para el procesamiento de imágenes
## Licencia
MIT
