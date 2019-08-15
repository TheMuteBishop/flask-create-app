class NewProject(object):

    def __init__(self, project_name, usermodel, base_dir):
        self.project_name = project_name
        self.usermodel = usermodel
        self.base_dir = base_dir or os.getcwd()
        self.context = {
            "project_name": self.project_name,
            "user": self.usermodel,
            "base_dir": base_dir,
            "secret_key": 'generate_secret_key()',
            "db_uri": None
            }
obj = NewProject("demo", False, 'sdad/safdsaf/ddfsf/')

def unpack(na,**kwargs):
    print(kwargs)

unpack('df',**obj.context)