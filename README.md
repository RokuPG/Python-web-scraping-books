# 📚 Book Scraper & API Service

El presente proyecto realiza **Web Scraping** dinámico sobre una tienda de libros, solicitando los titulos y precios de los libros en tiempo real y presentar los datos en formato JSON a través de una **API REST** construida con FastAPI.

## 🚀 Características
* **Extracción de datos:** Obtiene títulos y precios en tiempo real.
* **API Moderna:** Documentación interactiva automática con Swagger UI.
* **Exportación:** Generación de reportes en formato CSV y JSON.

## 🛠️ Tecnologías
* [Python 3.12+](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/) - Framework web.
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - Scraping.
* [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI.

## 📋 Requisitos previos
* Tener Python 3.10 o superior instalado.
* Conexión a internet (para que el scraper pueda acceder a la web).

## 📦 Instalación
1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Inicia el servidor: `uvicorn main:app --reload`

## 🛣️ Endpoints
| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Mensaje de bienvenida y comprobación del funcionamiento. |
| GET | `/libros` | Lista de libros extraídos en tiempo real. |