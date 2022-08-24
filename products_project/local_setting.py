
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t!)^_a!@7(7hw728$s$y@8t^inxa5rb0i^5z4s^2imr99a+ov7'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'product_database',
        'USER': 'root',
        'PASSWORD': 'AteDarling1!!!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}