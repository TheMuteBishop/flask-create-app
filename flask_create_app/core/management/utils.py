import secrets
import os
def generate_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join(secrets.choice(chars) for i in range(32))

def create_directory(dir_name):
    os.makedirs(dir_name, exist_ok=True)

def get_temp_dir(tmp_dir):
    return os.path.join( os.path.dirname(__file__),
        'templates', f'{tmp_dir}_template')

def get_app_file(name):
    template_dir = os.path.join( os.path.dirname(__file__),
                    'templates', f'app_template')
    for root, _, files in os.walk(template_dir):
        for file_name in files:
            filename, _ = os.path.splitext(file_name)
            if filename == name:
                return os.path.join(root, file_name)
    return None
