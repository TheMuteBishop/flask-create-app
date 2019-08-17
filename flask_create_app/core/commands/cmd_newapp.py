from flask_create_app.core.management.utils import get_temp_dir
from jinja2 import Environment, FileSystemLoader
import os
import click

from flask_create_app.core.management.utils import get_app_file, \
    create_directory

class NewApp(object):

    def __init__(self, app_name, base_dir):
        self.app_name = app_name
        self.base_dir = base_dir or os.getcwd()
        self.context = {
            "app_name": self.app_name,
            "base_dir": base_dir
            }

    def create_app(self):
        self.new_model_file()
        self.new_view_file()
        self.new_html_file()
    
    def template_parser(self,temp_path, temp_file, new_file):
        loader = FileSystemLoader(temp_path)
        env = Environment(loader=loader)
        temp = env.get_template(temp_file)
        with open(new_file, 'w', encoding='utf-8') as f:
            f.write(temp.render(**self.context))

    def new_model_file(self):
        filepath, tmp_file = os.path.split(get_app_file('model'))
        if tmp_file:
            new_path = os.path.join(self.base_dir, 'app', 'models')
            new_file_name = os.path.join(new_path, self.app_name + '.py')
            self.template_parser(filepath, tmp_file, new_file_name)
    
    def new_view_file(self):
        filepath, tmp_file = os.path.split(get_app_file('view'))
        if tmp_file:
            new_path = os.path.join(self.base_dir, 'app', 'views')
            new_file_name = os.path.join(new_path, self.app_name + '.py')
            self.template_parser(filepath, tmp_file, new_file_name)

    def new_html_file(self):
        filepath, tmp_file = os.path.split(get_app_file('index'))
        if tmp_file:
            new_path = os.path.join(self.base_dir, 'app', 'templates', self.app_name)
            create_directory(new_path)
            new_file_name = os.path.join(new_path, 'index.html')
            self.template_parser(filepath, tmp_file, new_file_name)


def create_new_app(app_name, project_dir, project_name=None):
    
    if project_name is not None:
        app_dir = os.path.join(project_dir, project_name, 'app')
        if not os.path.isdir(app_dir):
            raise ValueError('"App" directory not found')
        newapp = NewApp(app_name, os.path.join(project_dir, project_name))
    else:
        newapp = NewApp(app_name, project_dir)
    newapp.create_app()