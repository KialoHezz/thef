#### Project Title
Thef

#### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

#### Prerequisites
 - Make a folder of your project(mkdir )

 - Inside the project folder create Django environment and activate (python3 -m venv ) and source /bin/activate

 - Either start your own project or use this project by: git clone https://github.com/KialoHezz/thef.git
 - To run python3 manage.py runserver or ./manage.py Another way:

        - Inside your project folder pip install django
        - django-admin startproject <name-of-project> .
        - django-admin startapp <name-of-app>

 - Deployment
 - heroku login : Enter the credentials

 - Add Procfile file at Your root directory Which contain : web: gunicorn .wsgi --log-file

 - Add runtime.txt Use to specific the backport of your python version which contain: python-3.8.10

 - Config whitenoise: Django Static Files settings: in setting.py BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(file)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
)

In middleware section :
        'whitenoise.middleware.WhiteNoiseMiddleware',


        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
then : pip install whitenoise

Add requirements.txt Contains all requirements Heroku will look ,for example : It should containe

    config==0.3.9
    dj-database-url==0.5.0
    Django==1.11
    django-bootstrap3==10.0.1
    django-heroku==0.3.1
    gunicorn==19.9.0
    Pillow==5.2.0
    psycopg2==2.7.5
    python-decouple==3.1
    pytz==2018.5
    whitenoise==4.0


- pip install django-heroku && pip freeze > requirements.txt

- pip install python-decouple

- pip install dj-database-url

 - Add .env Which will contain the following environment variables SECRET_KEY DEBUG DB_NAME DB_USER DB_PASSWORD DB_HOST MODE='dev' #set to 'prod' in production ALLOWED_HOSTS='*' DISABLE_COLLECTSTATIC=1

- heroku create

- heroku addons:create heroku-postgresql:hobby-dev

- heroku config:set (cat .env | sed '/^/d; /#[[:print:]]*$/d')

- git add .

- git commit -m "message"

- git push origin master:main

-- Run migrations

- heroku run python manage.py migrate
- heroku pg:push DATABASE_URL --app
- Versioning
- Python-3.8.10 Acknowledgments Inspiration{Documentation}
- Python-3.10

#### Authors
Hezron Ngoma $ Isaac Wangombe - Initial work - Thef

#### License
This project is licensed under the HEZZYKIALO $ isaacmariga  License Copyright &copy 2022-HNK-isaacmariga