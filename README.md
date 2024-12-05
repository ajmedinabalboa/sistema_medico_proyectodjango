# sistema_medico_proyectodjango
Proyecto con Djando para el modulo 5 del Diplomado en FullStack

# Sistema Médico

Este es un proyecto básico de sistema de administración médica desarrollado con Django y Django Rest Framework (DRF). Incluye funcionalidades para gestionar pacientes, médicos, citas médicas y sus historiales.

## Requisitos

- Python 3.8 o superior
- Django 4.0 o superior
- Django Rest Framework

## Instalación

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/ajmedinabalboa/sistema_medico.git
   cd sistema_medico

2. Crear un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    venv\Scripts\activate

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt

4. Realizar las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Crear un superusuario:
   ```bash
   python manage.py createsuperuser

6. Iniciar el servidor:
   ```bash
      python manage.py runserver

## Funcionalidades

Gestión de pacientes, médicos, citas y historiales médicos.
API REST para interactuar con el sistema:
CRUD de pacientes, médicos y citas.
Consulta personalizada de pacientes adultos.
Endpoints Principales
api/pacientes/ - Gestión de pacientes.
api/medicos/ - Gestión de médicos.
api/citas/ - Gestión de citas.
api/adultos/ - Consulta personalizada de pacientes adultos.
