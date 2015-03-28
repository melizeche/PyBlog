# PyBlog
Ejemplo de aplicación de blog presentado en el #PyDayAsuncion

## Requisitos
### Django y Git
* tl;dr Para ubuntu

sudo apt-get install python-django git

* En general

https://www.djangoproject.com/download/

## Pasos para ejecutar

```
git clone https://github.com/melizeche/PyBlog.git
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

Ingresar en el browser a 

`http://localhost:8000`

y

`http://localhost:8000/admin`
