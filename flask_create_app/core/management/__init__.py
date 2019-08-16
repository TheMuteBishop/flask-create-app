import os
import click
def get_temp_dir(tmp_dir):
    return os.path.join( os.path.dirname(__file__),'templates', f'{tmp_dir}_template')


