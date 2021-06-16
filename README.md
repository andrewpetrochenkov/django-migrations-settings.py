[![](https://img.shields.io/badge/released-2021.6.15-green.svg?longCache=True)](https://pypi.org/project/django-migrations-settings/)
[![](https://img.shields.io/badge/license-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)

### Installation
```bash
$ pip install django-migrations-settings
```

### Pros
+   standalone migrations settings without project and database

### Cons
+   migrations history not supported

### How it works
key|value
-|-
`INSTALLED_APPS`|`setuptools.find_packages()` without `.`

### Examples
```bash
$ export DJANGO_SETTINGS_MODULE='django_migrations_settings'
$ django-admin.py makemigrations
```

