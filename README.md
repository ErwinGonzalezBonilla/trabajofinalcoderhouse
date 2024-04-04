°Inicio del proyecto Final del Curso de Python en CODERHOUSE
°Creación del proyecto Django1 en Visual estduio Code

°Creación del entorno virtual 
python -m venv 

°Carpeta distibuible y crear la base de datos en db.sqlite3
python setup.py sdist

°Creo mi proyecto en Github trabajofinalcoderhouse
git clone https://github.com/ErwinGonzalezBonilla/trabajofinalcoderhouse

°Activo mi entorno virtual
python3 -m venv .venv
source .venv/bin/activate
cd src
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

°Creo mi carpeta 'productos' con esto empiezo a confeccionar mi tienda de Trompetas
Creo las URLs en urls.py.
Definimos las clases y funciones de las vistas en views.py como tambien las renderizaciones.
En models.py creamos el modelo de cliente, utilizando CharField, TextField para definir los tipos de datos que seran almacenados en la base de datos.
Utilizando así herencia de modelos y la herencia de vistas (herencia de plantillas).

°Procedemos a ejecutar las migraciones 
python manage.py makemigrations productos   
python manage.py migrate productos

°Creamos Templates, en esta carpeta abierta en la aplicacion productos creamos los archivos:
product_detail.html
product_list.html

°Se crea el Superadministrador
python manage.py createsuperuser    

°Definimos la pantalla principal donde se encuentra un menú con:
- Tienda de Trompetas
- Instrumentos
- Accesorios
- Acerca de mi
- Login
- Logout

°Se crea el modelo principal que muestra todos los productos en Stock. Luego se distribuyen 
los productos por categorias, en este caso entre 'Instrumentos' y 'Accesorios'.
Cada producto tiene un boton donde se muestra las caracteristicas de los mismos detalladamente. 

°En 'Acerca de mi' hablo un poco sobre mi persona.

°Se crea en el proyecto otra carpeta
python manage.py startapp usuario
Ahí se confecciona el login y el logout.
'Login' solicita nombre y contrasenia.
'Logout' permite desloguearse 'Te deslogueaste correctamente'.

°Se crean los templates : login.html y logout.html 
AuthenticationForm es utilizado en urls.py de 'usuario'.

A mi pagina web Tienda de Trompetas le falta confeccion y detalles,igual me falta mucho por aprender,
este curso es mi iniciación al mundo de la programación, pero creo que es un buen proyecto para su evaluación, espero cumpla con sus espectativas y aprobación. 

Anexo video de muestra: 




