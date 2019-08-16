from flask_create_app.core.management import get_temp_dir
from jinja2 import Template
import os
import shutil
import click
from flask_create_app.core.management.utils import generate_secret_key
class NewProject(object):

    def __init__(self, project_name, usermodel, base_dir):
        self.project_name = project_name
        self.usermodel = usermodel
        self.base_dir = base_dir or os.getcwd()
        self.context = {
            "project_name": self.project_name,
            "user": self.usermodel,
            "base_dir": base_dir,
            "secret_key": generate_secret_key(),
            "db_uri": None
            }

    def template_parser(self,old_file, new_file):
        click.echo(f'writinh {old_file} .... \n')
        with open(old_file, 'r') as f:
            template = Template(f.read())
            content = template.render(**self.context)
        with open(new_file, 'w', encoding='utf-8') as f:
            f.write(content)

    def create_project(self):
        template_dir = get_temp_dir('project')
        top_dir = self.base_dir
        temp_dir_len = len(template_dir) + 1
        for root, dirs,files in os.walk(template_dir):
            for file_name in files:
                filename, file_extension = os.path.splitext(file_name)
                if file_extension in ['.html', '.py', '.py-tpl', '.css']:
                    rel_dir = root[temp_dir_len:]
                    new_path = os.path.join(top_dir, self.project_name, rel_dir)
                    old_file = os.path.join(root, file_name)
                    if file_extension in ['.html', '.css']:
                        new_file = os.path.join(new_path, file_name)
                        self.create_directory(new_path)
                        shutil.copy(old_file, new_file)
                    elif not self.usermodel and 'account' in root:
                        pass
                    else:
                        self.create_directory(new_path)
                        if file_extension == '.py-tpl':
                            new_file = os.path.join(new_path, filename + '.py')
                        else:
                            new_file = os.path.join(new_path, filename + file_extension)
                        self.template_parser(old_file, new_file)
                        
    def create_directory(self,dir_name):
        os.makedirs(dir_name, exist_ok=True)

def print_to_consol(msg):
    click.echo(msg)

def create_project(name, user, base_dir):
    np = NewProject(name, user, base_dir)
    np.create_project()

            