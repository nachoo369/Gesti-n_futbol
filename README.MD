# Sistema de Gestión de Torneos de Fútbol (RegistroFutbol)

Este proyecto es un sistema de gestión para torneos y partidos de fútbol, construido con Django 5.2 y Django REST Framework (DRF) para ofrecer tanto una interfaz web (CRUD) como una API RESTful.

## Características

* **Gestión de Jugadores:** Crea, lista, edita y elimina información de jugadores, incluyendo su foto, posición, edad, país y equipo.
* **Gestión de Equipos:** Crea, lista, edita y elimina equipos, incluyendo su escudo, entrenador y país.
* **Gestión de Torneos:** Crea torneos, asigna equipos participantes, y visualiza la información del torneo.
* **Gestión de Partidos:** Registra partidos con equipos locales/visitantes, goles y asociado a un torneo.
* **API RESTful:** Acceso programático a los datos de jugadores, equipos, torneos, partidos y países a través de endpoints REST.
* **Interfaz Web Amigable:** Utiliza Tailwind CSS para un diseño moderno y responsivo.

## Tecnologías Utilizadas

* **Backend:** Django 5.2.4
* **API:** Django REST Framework 3.x
* **Base de Datos:** SQLite3 (por defecto para desarrollo, fácilmente configurable para PostgreSQL/MySQL)
* **Frontend:** HTML, CSS (Tailwind CSS), JavaScript (si aplica alguna lógica específica)
* **Manejo de Archivos:** Pillow (para ImageFields)

## Requisitos Previos

Asegúrate de tener Python 3.9+ instalado en tu sistema.

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

1.  **Clona el repositorio:**
    ```bash
    git clone [URL_DE_TU_REPOSITORIO]
    cd registro_futbol
    ```
    *(Si lo descargaste como ZIP, simplemente descomprime y navega a la carpeta principal `registro_futbol`.)*

2.  **Crea un entorno virtual:**
    Es una buena práctica aislar las dependencias de tu proyecto.
    ```bash
    python -m venv env
    ```

3.  **Activa el entorno virtual:**
    * **Windows:**
        ```bash
        .\env\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source env/bin/activate
        ```

4.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Si no tienes un `requirements.txt`, puedes crearlo con `pip freeze > requirements.txt` después de instalar `django` y `djangorestframework`, o simplemente instala las librerías directamente: `pip install django djangorestframework Pillow django-select2`)*

5.  **Configura la base de datos y migra:**
    ```bash
    python manage.py makemigrations futbol
    python manage.py migrate
    ```

6.  **Crea un superusuario (administrador):**
    Necesitarás esto para acceder al panel de administración de Django y crear datos iniciales.
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las indicaciones para crear tu usuario.

7.  **Crea directorios para archivos multimedia (si no existen):**
    Asegúrate de que las carpetas `media/jugadores/` y `media/escudos/` existan para que Django pueda guardar las imágenes.
    ```bash
    mkdir -p media/jugadores
    mkdir -p media/escudos
    ```
    *(`mkdir -p` crea los directorios si no existen. En Windows puedes usar `md media\jugadores` y `md media\escudos`)*

8.  **(Opcional) Agrega imágenes de placeholder:**
    Para que las plantillas de lista de jugadores y equipos se vean bien incluso sin imágenes subidas, coloca las imágenes de placeholder por defecto en la siguiente ruta:
    * `futbol/static/futbol/default_player.png`
    * `futbol/static/futbol/default_team.png`

## Uso

1.  **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El servidor estará disponible en `http://127.0.0.1:8000/`.

2.  **Panel de Administración:**
    Accede al panel de administración de Django en `http://127.0.0.1:8000/admin/` con el superusuario que creaste. Aquí puedes crear y gestionar Países, Jugadores, Equipos, Torneos y Partidos. Es **recomendable** que crees algunos datos de prueba antes de explorar las vistas de la aplicación.

3.  **Interfaz Web:**
    * Página de inicio: `http://127.0.0.1:8000/`
    * Lista de Jugadores: `http://127.0.0.1:8000/jugadores/`
    * Lista de Equipos: `http://127.0.0.1:8000/equipos/`
    * Y las demás URLs de CRUD (crear/editar/eliminar) y creación de torneos/partidos.

4.  **API RESTful:**
    Puedes acceder a la API en las siguientes rutas:
    * Lista de Jugadores: `http://127.0.0.1:8000/api/jugadores/`
    * Detalle de Jugador: `http://127.0.0.1:8000/api/jugadores/<id>/` (ej. `http://127.0.0.1:8000/api/jugadores/1/`)
    * Lista de Equipos: `http://127.0.0.1:8000/api/equipos/`
    * Detalle de Equipo: `http://127.0.0.1:8000/api/equipos/<id>/`
    * Lista de Torneos: `http://127.0.0.1:8000/api/torneos/`
    * Lista de Partidos: `http://127.0.0.1:8000/api/partidos/`
    * Lista de Países: `http://127.0.0.1:8000/api/paises/`
    * Detalle de País: `http://127.0.0.1:8000/api/paises/<id>/`