from app import db


USER_USERNAME = 'Username'
USER_PASSWORD = 'Password'
USER_FIRST_NAME = 'First name'
USER_LAST_NAME = 'Last name'
USER_EMAIL = 'Email'
USER_IS_ACTIVE = 'Is active'
USER_IS_ADMIN = 'Is admin'


class AbstractUser(db.Model):
    """

    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(USER_USERNAME, db.String(64), unique=True)
    password = db.Column(USER_PASSWORD, db.String(64))


class User(AbstractUser):
    """

    """

    first_name = db.Column(USER_FIRST_NAME, db.String(64))
    last_name = db.Column(USER_LAST_NAME, db.String(64))
    email = db.Column(USER_EMAIL, db.String(128), nullable=False, unique=True)
    is_admin = db.Column(USER_IS_ADMIN, db.Boolean())
    is_active = db.Column(USER_IS_ACTIVE, db.Boolean())

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    def __repr__(self):
        return f'<User {self.get_full_name()}>'

    def __str__(self):
        return f'{self.username}'
