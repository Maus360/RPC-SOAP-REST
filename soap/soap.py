python_home = "/home/maus/.local/share/virtualenvs/rpc-soap-bb8Vm2wN"
activate_this = python_home + "/bin/activate_this.py"
exec(compile(open(activate_this, "rb").read(), activate_this, 'exec'), dict(__file__=activate_this))

from main import wsgi_app
application = wsgi_app
