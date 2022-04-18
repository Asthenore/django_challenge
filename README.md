# Django Backend Code Challenge
Create templates and generate dynamic emails based on the user associated with the email

## Running Locally

```bash
git clone https://github.com/Asthenore/django_challenge.git
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py runserver
```

Now open the Django admin in a web browser: 127.0.0.1:8000/admin/

## For the aplication test

### Log in with the superuser credentials
### For the staff user: 
Create an user using the user app at: http://127.0.0.1:8000/admin/user_app/customuser/add/, give it staff status, fill the email field in personal info.
### For the regular user: 
Create an user using the user app at: http://127.0.0.1:8000/admin/user_app/customuser/add/, fill the personal info with First name = "Juan" and Last name = "Pérez"

### For the templeate: 
Create a template using the email app at :http://127.0.0.1:8000/admin/email_app/emailtemplate/add/, fill the subject field with "{{ user.get_full_name }}, welcome to the new Python Course!", fill the content field with "This email is intended for {{ user.inverted_name }},
We are pleased to let you know that you have been selected to participate in our
new Python Course. Please send us your information and documents to
complete the registration process to continue with the course. In addition, we
have attached the course syllabus to this email.
You have seven days from now ({{ timestamp }}) to complete the registration.
Greetings from Python School!". In attachments select and upload any file.

### Log out from the superuser acount, log in as the staff user and create an email at: http://127.0.0.1:8000/admin/email_app/email/add/, select the email template and the user Juan Pérez. Save and continue editing to render the template.
