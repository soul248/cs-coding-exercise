# Define the application directory
import os, time

os.environ['TZ'] = 'America/Mexico_City'
time.tzset()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Statement for enabling the development environment
DEBUG = True

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI        = "mysql://cscodingexercise:cscodingexercise@mysql:3306/cscodingexercise?charset=utf8mb4"
SQLALCHEMY_ECHO                = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS       = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for signing the data. 
CSRF_SESSION_KEY = "adf90ab109117ab0c951c8b34bc4f5863104badb56eba27735ee5a6f20a28b9e"

# Secret key for signing cookies
SECRET_KEY = "581f79e9c6a9cb25564f153181700a9785367e109ac961fcc7160f1afc3edf33"