# Django REST framework service backend template

**Why?**

Standard Django comes with a lot of batteries, but even with them it's up to you to implement such basic features like:
* Auth workflow, Login/Registration
* Custom user model
* CORS + JWT

This features implemented in this template:

Features:
- Custom user model
- JWT auth via `simple-JWT`
- Local settings
- CORS
- Login and registration views

---
Planned:
- Change password view
- Reset password view
- User notification mechanism
- Docker
- CI-CD
- Swagger (?)
- Sentry (?)

## Pre-requisites:

**Required**
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

**Optional**
- [JWT](https://jwt.io/)
- [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

## Installation


``` (bash)
pip install -r requirements.txt
cd ./src/core
echo local_settings.template.py > local_settings.py
python src/manage.py test
```

## Usage

### Codestyle: 
[//]: # (Taken from https://github.com/f213/education-backend)

### Style

* [Django codestyle](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style).
* Use docstrings.

### Code organisation

* KISS + DRY.
* Use [Django best practices](http://django-best-practices.readthedocs.io/en/latest/index.html).
* Make fat models. **Don't write business-logic in views**. 
* Use PEP-484 [type-hints](https://www.python.org/dev/peps/pep-0484/) when possible.
* Use [GenericRelations](https://docs.djangoproject.com/en/1.10/ref/contrib/contenttypes/)
* Use [Manager](https://docs.djangoproject.com/en/1.10/topics/db/managers/)
* Don't use [signals](https://docs.djangoproject.com/en/1.10/topics/signals/) for business logic.
* Use [django translation](https://docs.djangoproject.com/en/1.10/topics/i18n/translation/).
* Put business logic in `service.py` files
