# Clínica Odontológica API
#Integrantes
- Ticona Nina Valeria Abigai
- Velasquez Puma Brigitte Karolay
## Descripción

Clínica Odontológica API es una aplicación web desarrollada con Django y Django REST Framework para la gestión interna de una clínica odontológica.

El sistema permite administrar pacientes, especialistas, especialidades, citas, historias clínicas, procedimientos, tratamientos sugeridos, presupuestos y pagos, proporcionando una API REST segura y documentada.

---

# Objetivos del Proyecto

* Gestionar la información de una clínica odontológica.
* Implementar una API REST utilizando Django REST Framework.
* Aplicar autenticación mediante JSON Web Token (JWT).
* Documentar automáticamente la API utilizando Swagger.
* Publicar el proyecto en Internet mediante Vercel.
* Aplicar los conceptos desarrollados en el libro mediante un proyecto real.

---

# Tecnologías Utilizadas

* Python
* Django
* Django REST Framework
* SQLite
* PostgreSQL
* Supabase
* Swagger
* drf-spectacular
* JWT
* Postman
* Vercel

---

# Estructura General del Sistema

El sistema está compuesto por las siguientes entidades:

* Patients
* Specialties
* Specialists
* Appointments
* Medical Records
* Procedures
* Suggested Treatments
* Budgets
* Budget Details
* Payments

---

# Funcionalidades Principales

* Gestión de pacientes.
* Gestión de especialidades odontológicas.
* Gestión de especialistas.
* Gestión de citas.
* Gestión de historias clínicas.
* Gestión de procedimientos.
* Gestión de tratamientos sugeridos.
* Gestión de presupuestos.
* Gestión de pagos.
* API REST.
* Documentación automática.
* Autenticación con JWT.
* Eliminación lógica mediante is_active.
* Deploy en la nube.

---

# Instalación del Proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/valeriatni/ClinicaOdontologicaAPI.git
cd ClinicaOdontologicaAPI
```

---

## 2. Crear entorno virtual

```bash
python -m venv myvenv
```

---

## 3. Activar entorno virtual

### Windows

```bash
myvenv\Scripts\activate
```

### Linux / Mac

```bash
source myvenv/bin/activate
```

---

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 5. Crear archivo .env

Crear un archivo llamado:

```text
.env
```

en la raíz del proyecto, al lado de:

```text
manage.py
```

Contenido:

```env
SECRET_KEY=django-insecure-your-secret-key
DEBUG=True
```

La clave secreta puede generarse mediante:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 6. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7. Crear superusuario

```bash
python manage.py createsuperuser
```

---

## 8. Ejecutar el proyecto

```bash
python manage.py runserver
```

La aplicación se ejecutará en:

```text
http://127.0.0.1:8000/
```

---

# Estructura del Proyecto

```text
ClinicaOdontologicaAPI
│
├── clinic/
├── config/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── .env
└── myvenv/
```

---

# Panel de Administración

Django Admin permite administrar los modelos registrados mediante una interfaz gráfica.

Ruta:

```text
http://127.0.0.1:8000/admin/
```

---

# API REST

Ruta principal:

```text
http://127.0.0.1:8000/api/
```

La API permite realizar operaciones CRUD sobre las entidades del sistema.

---

# Documentación Automática

## Swagger UI

Genera documentación automática e interactiva de la API.

Permite visualizar y probar los endpoints del sistema.

Ruta:

```text
http://127.0.0.1:8000/api/schema/swagger-ui/
```
---

## OpenAPI Schema

Genera el esquema completo de la API.

Ruta:

```text
http://127.0.0.1:8000/api/schema/
```

---

# Endpoints Principales

## Patients

```text
http://127.0.0.1:8000/api/patients/
```

Permite gestionar los pacientes registrados.

---

## Specialties

```text
http://127.0.0.1:8000/api/specialties/
```

Permite gestionar las especialidades odontológicas.

---

## Specialists

```text
http://127.0.0.1:8000/api/specialists/
```

Permite gestionar los especialistas de la clínica.

---

## Appointments

```text
http://127.0.0.1:8000/api/appointments/
```

Permite registrar y administrar las citas odontológicas.

---

## Medical Records

```text
http://127.0.0.1:8000/api/medical-records/
```

Permite gestionar la historia clínica de cada paciente.

---

## Procedures

```text
http://127.0.0.1:8000/api/procedures/
```

Permite gestionar los procedimientos odontológicos disponibles.

---

## Suggested Treatments

```text
http://127.0.0.1:8000/api/suggested-treatments/
```

Permite registrar tratamientos sugeridos.

---

## Budgets

```text
http://127.0.0.1:8000/api/budgets/
```

Permite administrar los presupuestos.

---

## Budget Details

```text
http://127.0.0.1:8000/api/budget-details/
```

Permite gestionar el detalle de los procedimientos incluidos en un presupuesto.

---

## Payments

```text
http://127.0.0.1:8000/api/payments/
```

Permite registrar pagos realizados por los pacientes.

---

# Autenticación JWT

El proyecto implementa autenticación mediante JSON Web Token.

## Generar Token

Ruta:

```text
http://127.0.0.1:8000/api/token/
```

Ejemplo:

```json
{
    "username": "admin",
    "password": "password"
}
```

---

## Refresh Token

Ruta:

```text
http://127.0.0.1:8000/api/token/refresh/
```

Permite renovar el token de acceso.

---

## Uso del Token

Las solicitudes protegidas requieren:

```text
Authorization: Bearer ACCESS_TOKEN
```

---

# Eliminación Lógica

El sistema utiliza el atributo:

```text
is_active
```

para activar o desactivar registros.

Ejemplo:

```http
PATCH /api/patients/1/
```

```json
{
    "is_active": false
}
```

De esta manera se conserva el historial de la información.

---

# Backup

El proyecto utiliza SQLite para la ejecución local.

La base de datos se encuentra en:

```text
db.sqlite3
```

Este archivo puede utilizarse como copia de seguridad.

---

# Variables de Entorno

El archivo:

```text
.env
```

permite almacenar información sensible fuera del código.

Variables utilizadas:

```env
SECRET_KEY=
DEBUG=
```

---

# Deploy en Vercel

El proyecto se encuentra desplegado en:

```text
clínica-odontológica-api-gf2w.vercel.app 
```

Para desplegar nuevamente:

1. Importar el repositorio en Vercel.
2. Configurar las variables de entorno:

```text
SECRET_KEY
DEBUG=False
```

3. Ejecutar Deploy.

---

# Cumplimiento del Libro

El proyecto implementa los principales conceptos estudiados:

* Entorno virtual.
* Instalación de dependencias.
* Modelos.
* Migraciones.
* Django Admin.
* Serializers.
* ViewSets.
* API REST.
* Routers.
* CRUD.
* Postman.
* Swagger.
* Archivo .env.
* Backup.
* JWT.
* Deploy en Vercel.

---

# Conclusión

Clínica Odontológica API es una aplicación desarrollada para la gestión interna de una clínica odontológica.

Mediante este proyecto fue posible aplicar los conceptos estudiados en el libro, integrando bases de datos, Django, APIs REST, autenticación, documentación automática y despliegue en la nube, obteniendo una solución completa y funcional.
