import uuid

from app import db, bcrypt
from app.models.user_model import User, Role, UsersRoles

def create_db():
    db.drop_all()
    db.create_all()

def create_new_user(username, email, password, is_admin=False ):
    # check table exists
    try:
        user = User.query.all()
    except OperationalError as e:
        return (False, e._message())
    user = User.query.filter_by(email=email).first()
    if user:
        return (False, f'{username} or {email} already exists. Try another one.')
    hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')

    newuser = User(username=username,public_id=str(uuid.uuid4()), email=email, password=hashed_pass, is_admin=is_admin)
    db.session.add(newuser)
    db.session.commit()
    return (True, newuser.username)

def create_super_user(username, email, password):
    return create_new_user(username, email, password,is_admin=True)