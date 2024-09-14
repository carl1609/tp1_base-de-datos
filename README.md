# Proyecto de Administración de Base de Datos

Este proyecto es una aplicación Django que permite la ejecución y monitoreo de consultas SQL en un servidor PostgreSQL. Incluye vistas para visualizar información sobre bases de datos, 
tablas, esquemas, funciones, y más.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

1. **Python**
2. **Django**: El proyecto está desarrollado en Django, por lo que debes tenerlo instalado.
3. **PostgreSQL**: El servidor de base de datos utilizado es PostgreSQL, por lo que deberás tenerlo instalado y un usuario postgres y base de datos postgres con contraseña 12345 o
   modificarlo en settings.py
5. **Git**: Para clonar el repositorio remoto, asegúrate de tener Git instalado.

## Instrucciones de instalación

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local. Abre una terminal y ejecuta el siguiente comando:
git clone <URL_DEL_REPOSITORIO>

### 2. Crear y activar un entorno virtual
cd <nombre_del_directorio_clonado>
python -m venv env

Para activar el entorno virtual:
En Windows: env\Scripts\activate
En Linux/macOS: source env/bin/activate

### 3. Instalar las dependencias
Con el entorno virtual activado, instala las dependencias del proyecto ejecutando el siguiente comando: pip install -r requirements.txt

### 4. Intala y configra PostgreSQL

### 5. Migraciones de base de datos
python manage.py migrate

### 6. Ejecutar el servidor
python manage.py runserver
El servidor estará disponible en http://localhost:8000.

## Uso de la aplicación
Una vez que el servidor esté corriendo, puedes acceder a la aplicación desde tu navegador. La aplicación te permitirá elegir dentro del menú y ejecutar las consultas SQL que eligas en tu
base de datos PostgreSQL y visualizar los resultados en tiempo real, así como generar gráficos para consultas específicas.

## Estructura del proyecto
views.py: Contiene la lógica de las vistas que ejecutan las consultas SQL y devuelven los resultados.
urls.py: Define las rutas de acceso a las diferentes vistas de la aplicación.
templates: Contiene los archivos HTML que muestran los resultados de las consultas y otros elementos visuales.
static: Archivos JavaScript y CSS utilizados para la interfaz de usuario.
