This is an application to teach an elementary knowledge of web applicatoion development using django framework.

***********
QUICK START
***********

1.  Add semiuscrumy to your INSTALLED APPS settings like This

    INSTALLED_APPS = [
        ...
        'semiuscrumy',
    ]

2.  Include the semiuscrumy URLConf in your project urls.py like This

    path('semiuscrumy', Include('semiuscrumy.urls'))

3.  Run 'python manage.py migrate' to create the models

4.  Start the development server and visit http://127.0.0.1:8000/admin to administer users
