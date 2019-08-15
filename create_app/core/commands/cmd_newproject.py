from create_app.core.management import get_temp_dir
from jinja2 import Template
import os
import shutil
import click
from create_app.core.management.utils import generate_secret_key
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

def template_parser(old_file, new_file):
    click.echo(f'writinh {old_file} .... \n')
    with open(old_file, 'r') as f:
        template = Template(f.read())
        content = template.render(self.context)
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(content)


def create_project(name, user):
    template_dir = get_temp_dir('project')
    top_dir = '/home/shiv/workplace/demo'
    temp_dir_len = len(template_dir) + 1
    temp_en = NewProject(name, user, top_dir)
    for root, dirs,files in os.walk(template_dir):
        for file_name in files:
            filename, file_extension = os.path.splitext(file_name)
            if file_extension in ['.html', '.py', '.py-tpl', '.css']:
                if file_extension in ['.html', '.css']:
                    rel_dir = root[temp_dir_len:]
                    new_path = os.path.join(top_dir, name, rel_dir)
                    create_directory(new_path)
                    old_file = os.path.join(root, file_name)
                    new_file = os.path.join(new_path, file_name)
                    shutil.copy(old_file, new_file)
                else:
                    rel_dir = root[temp_dir_len:]
                    new_path = os.path.join(top_dir, name, rel_dir)
                    create_directory(new_path)
                    old_file = os.path.join(root, file_name)
                    new_file = os.path.join(new_path, filename + '.py')
                    temp_en.template_parser(old_file, new_file)

def create_directory(dir_name):
    os.makedirs(dir_name, exist_ok=True)

def template_parser(old_file, new_file, **ctx):
    click.echo('template_parser')
    # with open(old_file, 'r') as f:
    #     template = Template(f.read())
    #     content = template.render(**ctx)
    # with open(new_file, 'w', encoding='utf-8') as f:
    #     f.write(content)

def print_to_consol(user):
    # file_name = '/home/shiv/workplace/baboo/create_app/core/management/templates/project_template/app/settings.py'
    # with open(file_name, 'r') as f:
    #     template = Template(f.read())
    #     click.echo(template.render(user=user))
    dir_name = '/home/shiv/workplace/baboo/create_app/core/management/templates/project_template'
    top_dir = '/home/shiv/workplace/demo'
    temp_dir_len = len(dir_name) + 1

    for root, dirs, files in os.walk(dir_name):
        for f in files:
            path_after_dir_name = root[temp_dir_len:]
            click.echo(os.path.join(top_dir ,path_after_dir_name))
            

            