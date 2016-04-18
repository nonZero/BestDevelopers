# What's going on here?

This is a simple demo project used to demonstrate basic Django 1.9 concepts 
during the "Djagno Crash Course" training session.

Check out the project's log to follow through different steps/stages in the 
projet's creation.

 
To create a new django Project we have used:

    mkdir BestDevelopers
    cd BestDevelopers
    django-admin startproject bestdevelopers .
     
     
We have used [m.cmd](m.cmd) on windows and `alias m="python manage.py"` on
linux/mac/*sh to create an `m` shortcut to [manage.py](manage.py).

To create migrations from new/modeified models:

    m makemigrations
    
And to apply them to the database:

    m migrate

To create a super user:

    m createsuperuser

## Other links:

- WSGI Example: <https://gist.github.com/nonZero/fd5c6ac97ce9ede20953c450e885bc5b>