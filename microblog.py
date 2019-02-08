from app import create_app, app, db
from app.models import User, Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

'''
With a regular interpreter session, the app symbol is not known unless
it is explicitly imported, but when using flask shell, 
the command pre-imports the application instance. 
The nice thing about flask shell is not that it pre-imports 
app, but that you can configure a "shell context", which is a 
list of other symbols to pre-import.
'''
'''
The app.shell_context_processor decorator registers the function 
as a shell context function. When the flask shell command runs, 
it will invoke this function and register the items returned 
by it in the shell session.
'''