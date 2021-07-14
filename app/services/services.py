from flask import current_app

def add_commit(clas):
    session = current_app.db.session

    session.add(clas)
    session.commit()