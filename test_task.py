from app import app, db
from app.models import Driver


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Driver': Driver}
