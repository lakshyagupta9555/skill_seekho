@echo off
del manage.py
copy manage_new.py manage.py
echo manage.py fixed!
venv\Scripts\activate && python manage.py runserver
