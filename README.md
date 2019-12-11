# travelling
In this repository I provide back-end python codes (Django package) as well as HTML, CSS and JS files the  travel agency web. It has two application called index and account. Account is an pplication for user sign-up, sign-in, sign-out functionalities. Index is used for visualization of the destinations in the homepage. 

Steps to Visualize the Web:

1. You need to install Python as well as PostGreSQL on your computer to visualize the web. 
2. Setting a localdatabase: 
Then you should make changes to DATABASES of the setting.py >>
It requires user name and the password you have created during installation of PostGreSQL. More importantly you need to install the Pgadmin to create database with specific name and you need to enter this name next to the "NAME" section. At the end you need to set the localhost and the port below given to you by PostGresSQL during installation.

As we 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database name',
        'USER':'your user name',
        'PASSWORD':'your password',
        'HOST': 'localhost',
        'PORT': 'your port',
      }
    }
2. You will also need the connector between Django and PostGreSQL which is called psycopg2. you can use pip tools in python to install  
   it by following command in cmd: 
   pip install psycopg2

3. You need to create migration by writing the following command in cmd:
   python manage.py makemigrations
4. Now you can craete tables for objects in the models by following command:
   python manage.py sqlmigrate index <migrationfilenumber>
   above the <migrationfilenumber> is the number which is put in the first part of name of created files in migration folder of index        folder. 
5. The last stem is migration by writing the following command in the cmd:
   python manage.py migrate
   Now you should be able to see the migrated files in your local database. You need to install Pgadmin to see it in your local 
   database.
6. Now open cmd and set your dir to test1 folder and run the manage.py by python as follow:
   python manage.py runserver
7. Open your browser and browse http://127.0.0.1:8000/
  
Enjoy your browsning ;)  
