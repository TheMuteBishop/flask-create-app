from setuptools import setup, find_packages

setup(
    name='Flask-create-app',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Jinja2',
    ],
    entry_points='''
        [console_scripts]
        flask-create-app=flask_create_app.app:cli
    ''',
)