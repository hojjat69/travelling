# travelling
In this repository I provide back-end codes including Django as well as HTML, CSS and JS files with images to create front-end of the web. This website is developed for Travel Agencies. It is able of dynamic visualization in the destinations and users part. 

Steps to Visualize the Web:

1. You need to install Python as well as PostGreSQL on your computer to visualize the web. Then you should make changes to the setting.py    according to the information you insert during PostGreSQL installation as follow:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your name',
        'USER':'your user name',
        'PASSWORD':'your password',
        'HOST': 'localhost',
        'PORT': 'your port',
      }
    }
2. You will also need the connector between Django and PostGreSQL which is called psycopg2. you can use pip of python to install it by        following command in cmd: 
   pip install psycopg2

3. You need to create migration by writing the following command in cmd:
   python manage.py makemigrations
4. Now you can craete tables for objects in the model by following command:
   python manage.py sqlmigrate index <migrationfilenumber>
   above the <migrationfilenumber> is the number which is put in the first part of name of created files in migration folder of index        folder. 
5. The last stem is migration by writing the following command in the cmd:
   python manage.py migrate
   Now you should be able to see the migrated files in your local database
6. Now open cmd and set your dir to test1 folder and run the manage.py by python as follow:
   python manage.py runserver
7. Open your browser and browse http://127.0.0.1:8000/
  
Enjoy your browsning ;)
