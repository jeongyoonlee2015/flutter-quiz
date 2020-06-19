# Backend for [flutter-quiz-app](https://github.com/jeongyoonlee2015/flutter-quiz-app) 


### Django (First Django Proejct)
* Django with [Heroku](https://devcenter.heroku.com/articles/django-app-configuration)

Django is a Python-based free and open-source web framework that follows the model-template-view (MVC) architectural pattern. <br>
The main goal of the framework is to work harder on creating a highly database-based website. <br>
It emphasizes the reusability of components, the pluggability of plug-ins, and rapid development.<br>
It also followed the principle of "Don't repeat yourself" (DRY).


### Terminal
```.bash
pip install gunicorn
pip install django-heroku
```
> Although Django alone can open the REST API, <br>
Django's run server is a test-only feature, which results in performance issues when used in an operating environment. <br> The operational mode requires an association with Web Server Gateway Interface (WSGI) middleware such as 'Gunicorn'.
    
### Settings.py

```.py
import django_heroku
# Activate Django-Heroku.
django_heroku.settings(locals())
```
