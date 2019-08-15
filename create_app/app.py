
import click
from flask import Flask
from flask.cli import FlaskGroup
import os

class Template(object):
    def __init__(self, home=None):
        self.home = os.path.abspath(home or '.')


# @click.group(cls=FlaskGroup, create_app=creat_app)
@click.group()

def cli():
    pass

@cli.command()
@click.argument('name')
@click.option('--user', '-um', help='Initialize with user model', is_flag=True, default=False)
def new(name, user):
    ''' create a flask project and starting template with usermodel

    '''
    # user = click.prompt('Do u want to include basic user model? [y/n]')
    # TODO: following
    # 1. get project name === YTS
    # 2. check if directory is provided
    # 3. user model === YTS
    # 4. check if project name is python module name
    # 5. create dirs
    # 

    # click.echo(user)
    from create_app.core.commands.cmd_newproject import create_project, print_to_consol
    create_project(name, user)
    # print_to_consol(user)
    click.echo(f' {name} , {user} ')

if __name__ == "__main__":
    cli()