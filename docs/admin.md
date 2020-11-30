# admin page
to create admin
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
now enter your username
enter your e-mail address
enter a password

to add the model to the admin site 
from .models import Post
admin.site.register(Post)