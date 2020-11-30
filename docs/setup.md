# setup
create project folder on desktop or documents
open VS code 
open new project folder 
open terminal
python -m venv venv 
venv\Scripts\Activate.Ps1
pip install django 
pip freeze > requirements.txt
django-admin startproject config .
to load up the web page type in teminal command below
python manage.py runserver
python manage.py startapp blog

# extras
to upgrade pip input command below
pip install -U pip 
after installing any new packages/upgrades use below command
pip freeze > requirements.txt
to check django version enter command below
python -m django --version
pip install ipython
pip freeze > requirements.txt
pip install django-crispy-forms 
put this in confirg settings installed apps "crispy_forms"
put this at the bottom of congig.settings CRISPY_TEMPLATE_PACK = 'bootstrap4'
add below to template...
{% load crispy_forms_tags %}

<form method="post" class="uniForm">
    {{ my_formset|crispy }}
</form>