
## Paso 1: Ejegir carpeta para el proyecto y el entorno
## Paso 2: En la carpeta para el proyecto hacer git clone
git clone https://github.com/danielh-wh/refugio-animales.git
## Paso 3: Crear entorno en la carpeta para el entorno
mkvirtualenv refugio -p=2.7
#### Confirmar que sea en python 2.7
python -V
## Paso 4: Desactivar e iniciar entorno
#### Para desactivar podemos hacer:
deactivate
#### Para iniciar podemos hacer
workon refugio
## Paso 5: instalamos dependencias con el entorno iniciado
pip install -r requeriments.txt
## Paso 6: crear usuario
Python2 manage.py createsuperuser,
Ingresar usuario y contraseña
## Paso 7: Iniciar el proyecto:
python2 manage.py runserver
## Paso 8: Para desactivar el proyecto:
Ctrl+c
