import setuptools

SECRET_KEY = '42'

INSTALLED_APPS = list(filter(lambda p:'.' not in p,setuptools.find_packages()))
