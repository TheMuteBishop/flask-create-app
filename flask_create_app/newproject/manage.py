from flask.cli import FlaskGroup
import click
import os

from flask_create_app.core.commands.cmd_newapp import create_new_app
from app import create_app
from app.commands.cmd_db import create_db, create_new_user, create_super_user

@click.group(cls=FlaskGroup, create_app=create_app)
@click.pass_context
def cli(ctx):
    os.environ['FLASK_ENV'] ='development'

@cli.command('init-db')
def init_db():
    ''' Drop all tables and re-create all
    '''
    create_db()
    click.echo('Databse is initialized ..!!')

@cli.command('createuser')
@click.option('--admin', is_flag=True, default=False, help='is admin user?')
def creat_user(admin):
    ''' create new user '''
    username = click.prompt('username :')
    if not username:
        raise click.UsageError("username must be provided.")
    email = click.prompt('email :')
    if not email:
        raise click.UsageError("email must be provided.")
    password = click.prompt('Password', hide_input=True, confirmation_prompt=True)
    if not password:
        raise click.UsageError("password must be provided.")
    if admin:
        success = create_super_user(username, email, password)
    else:
        success = create_new_user(username, email, password)
    if not success[0]:
        raise click.UsageError(success[1])
    click.echo(f'{success[1]} created succefully ..!!')
    
@cli.command('startapp')
@click.argument('app_name')
def new_app(app_name ):
    """create new app in existing project
    """
    proj_dir = os.getcwd()
    create_new_app(app_name, proj_dir)


if __name__ == "__main__":
    cli()