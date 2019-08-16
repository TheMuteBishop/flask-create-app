
import click
import os

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name', nargs=-1)
@click.option('--user', '-um', help='Initialize with user model', is_flag=True, default=False)
def new(name, user):
    ''' create a flask project and starting template with usermodel

    '''
    if len(name) == 0 or len(name) > 2 :
        raise click.BadParameter('provide project name and directory only', param_hint='NAME , PROJECTDIR')
    elif len(name) == 1:
        project_name = name[0]
        base_dir = os.getcwd()
    else:
        project_name = name[0]
        base_dir = os.path.join(os.getcwd(), name[1])
    from flask_create_app.core.commands.cmd_newproject import create_project, print_to_consol
    create_project(project_name, user, base_dir)
    click.echo(f' {project_name} , {user} ')

if __name__ == "__main__":
    cli()