# Темплейт для разработки бэкендов на DRF

**Мотивация**

В стандартной джанге много батареек, но даже с ними приходится с нуля писать такие общие для веб-приложений вещи как:
* Аутентификация
* Подтверждение пароля
* Подключение CORS / JWT

Задача темплейта — дать общие функциональности из коробки.

В темплейте есть:
- Модель кастомного пользователя
- Аутентификация по JWT
- Локальные настройки
- CORS
- Вью для регистрации и логина

## Пре-реквезиты:

**Основное**
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

**Дополнительно**
- [JWT](https://jwt.io/)
- [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

## Установка


``` (bash)
pip install -r requirements.txt
cd ./src/core
echo local_settings.template.py > local_settings.py
```

## Использование

### Кодстайл: 
[//]: # (Taken from https://github.com/f213/education-backend)

### Стиль

* [Кодстайл Джанго](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style).
* Докстринги к моделям и методам.

### Организация кода

* KISS и DRY.
* Используйте [лучшие практики Джанго](http://django-best-practices.readthedocs.io/en/latest/index.html).
* Делайте толстые модели. **Без логики во вью**. Только модели.
* Используйте PEP-484 [тайп-хинты](https://www.python.org/dev/peps/pep-0484/) когда возможно.
* Используйте [GenericRelations](https://docs.djangoproject.com/en/1.10/ref/contrib/contenttypes/)
* Используйте [Manager](https://docs.djangoproject.com/en/1.10/topics/db/managers/)
* Не используйте [сигналы](https://docs.djangoproject.com/en/1.10/topics/signals/) для бизнес логики, используйте их для уведомлений.
* Используйте [django translation](https://docs.djangoproject.com/en/1.10/topics/i18n/translation/).