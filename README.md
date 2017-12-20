# isl2k17

Manual para configurar y correr esta aplicacion web
Como prerequisito, se requiere tener python instalado y actualizado. Tambien se asume que git esta instalado y correctamente configurado.

1) Instalar Virtualenv:
$ [sudo] pip install virtualenv
Si este paso no funciona, el pip esta desactualizado o no esta instalado, en cuyo caso descargar este archivo:
https://bootstrap.pypa.io/get-pip.py
Y correrlo de la siguiente forma
$ python get-pip.py
Y volver a intentar instalar el virtualenv

2) Instalar Django:
$ [sudo] pip install Django
Comprobar que se instalo con:
$ [sudo] python -m django --version
Que debería devolver la version de django instalada en caso que la instalacion haya sido exitosa

3) Clonar el repositorio:
Posicionado en un directorio donde se desee clonar el repositorio, correr:
$ [sudo] git clone https://github.com/daadnn/isl2k17.git

4) Moverse al raiz de la aplicacion:
$ cd isl2k17/flack

5) Antes de correr el servidor por primera vez, se necesitan configurar la base de datos (tambien correrlo si se pulleo del repositorio):
Correr los siguientes comandos
$ [sudo] python manage.py migrate

6) Ahora esta todo configurado, para correr el servidor simplemente hacer:
$ [sudo] python manage.py runserver

7) Para acceder, desde un navegador entrar a:
localhost:8000

8) Opcional, para crear un superusuario:
$ [sudo] python manage.py createsuperuser
Y seguir las instrucciones por pantalla.



