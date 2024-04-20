Para instalar el sistema se debe de seguir los siguientes pasos.
crear el entorno virtual en python:
- Instalar virtualevn: pip install virtualenv.
-Crear un nuevo directorio para el proyecto(opcional)
-Activar el entorno virtual.
Windows: nombredelentorno\Scripts\Activate.
linux: nombredelentorno/bin/activate.

Despues instalar los requerimientos.
Windows : pip install -r requirements.txt
Linux : pip install -r requirements.txt
Tener python 3.10.12



Para ejecutar la aplicacion web.

Dirigirse hasta manage.py.
para crear la bd: python3 manage.py migrate

para llegar ahi, automatas2-Proyecto/sistemaa/app/

para crear el usuario se usa el comando: python3 manage.py createsuperuser
y ejecutar el comando: python3 manage.py runserver




