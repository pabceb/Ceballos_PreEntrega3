Proyecto PreEntrega 3 de Pablo Ceballos

NOTAS: 
para modificaciones en models -->
python manage.py makemigrations

y para que impacten esas migraciones
python manage.py migrate

CORRECCIÓN DE README.MD
1. Crear una carpeta para guardar el proyecto.
2. Abrir carpeta con VSC
3. Crear .gitignore: usar gitignore.io --> apps --> gitignore auto-generado
4. Crear entorno virtual: python -m venv .nombre_entorno
5. Agregar nombre de carpeta de entorno virtual
6. Inicializar git (git init)
7. Crear primer commit
8. Conectar con repositorio en la nube
9. Generar primer push
10. Activar entorno virtual:
11. Instalar Django con el manejador de paquete de python ("pip install django")
12. Crear requirements.txt con dependencias (pip freeze > requirements.txt)
13. Crear el proyecto Django donde se está trabajando --> ´django-admin startproject nombre_proyecto .´ (no olvidar el "." del final)
14. Probar el proyecto con python manage.py migrate y luego con python manage.py runserver
15. Crear una aplicación principal (inicio) python manage.py startapp nombre_app
16. Agregar la app al archivo settings.py
17. Crear archivo inicio/urls.py
18. Agregar path para conectar el urls.py con el inicio/urls.py
path('url', include('nombre de la app'))
19. Agregar el valor 'BASE_DIR / "templates" a la key de DIRS dentro de la lista de la variable TEMPLATES en settings.py
20. Crear carpeta /templates
21. Crear VISTAS
- crear el path para conectar la vista en urls.py de la app
- crear la vista en archivo views.py de la app correspondiente
- crear el template que se utiliza para la vista dentro de /templates
- agregar el link/acceso html <a> al path que corresponda.

PENDIENTE: 
- models y forms
