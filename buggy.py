from app.__init__ import app , db
from app.models.models import User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}