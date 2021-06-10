import datetime as dt

from flask_login import UserMixin
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import ARRAY
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class ModelCrud:
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Role(db.Model, ModelCrud):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(31), nullable=False)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'<Role ({self.name})>'


class User(UserMixin, db.Model, ModelCrud):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(63), nullable=False)
    email = db.Column(db.String(127), nullable=False)
    password_hash = db.Column(db.String(127), nullable=False)
    profile_picture_path = db.Column(db.String(127), default='profiles/default.png', nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), default=10)
    last_seen = db.Column(db.DateTime, default=dt.datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User ({self.username})>'


db.Index('ix_users_username', func.lower(User.username), unique=True)
db.Index('ix_users_email', func.lower(User.email), unique=True)


class Spell(db.Model, ModelCrud):
    __tablename__ = 'spells'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63), index=True, unique=True, nullable=False)
    source = db.Column(db.String(15))
    tags = db.Column(ARRAY(db.String(31)), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    level_string = db.Column(db.String(7), nullable=False)
    school = db.Column(db.String(15), nullable=False)
    ritual = db.Column(db.Boolean, nullable=False, default=False)
    casting_time = db.Column(db.String(127), nullable=False)
    range = db.Column(db.String(63), nullable=False)
    components = db.Column(db.String(), nullable=False)
    duration = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text, nullable=False)
    at_higher_levels = db.Column(db.Text)
    url_path = db.Column(db.String(63), nullable=False, unique=True)
    srd = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Spell ({self.name})>'


class Creature(db.Model, ModelCrud):
    __tablename__ = 'creatures'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63), index=True, unique=True, nullable=False)
    tags = db.Column(ARRAY(db.String(63)), nullable=False)
    size = db.Column(db.String(15), nullable=False)
    kind = db.Column(db.String(15), nullable=False)
    sub_kind = db.Column(db.String(31))
    alignment = db.Column(db.String(31), nullable=False)
    armor_class = db.Column(db.Integer, nullable=False)
    armor_type = db.Column(db.String(63))
    hit_points = db.Column(db.String(63), nullable=False)
    hit_dice = db.Column(db.String(15))
    speed = db.Column(db.String(63), nullable=False)
    str = db.Column(db.Integer, nullable=False)
    str_mod = db.Column(db.Integer, nullable=False)
    dex = db.Column(db.Integer, nullable=False)
    dex_mod = db.Column(db.Integer, nullable=False)
    con = db.Column(db.Integer, nullable=False)
    con_mod = db.Column(db.Integer, nullable=False)
    int = db.Column(db.Integer, nullable=False)
    int_mod = db.Column(db.Integer, nullable=False)
    wis = db.Column(db.Integer, nullable=False)
    wis_mod = db.Column(db.Integer, nullable=False)
    cha = db.Column(db.Integer, nullable=False)
    cha_mod = db.Column(db.Integer, nullable=False)
    saving_throws = db.Column(db.String(63))
    damage_resistances = db.Column(db.String(255))
    damage_immunities = db.Column(db.String(255))
    condition_immunities = db.Column(db.String(255))
    damage_vulnerabilities = db.Column(db.String(255))
    skills = db.Column(db.String(255))
    senses = db.Column(db.String(255))
    languages = db.Column(db.String(255))
    cr_string = db.Column(db.String(3), nullable=False)
    cr = db.Column(db.Float, nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    source = db.Column(db.String(63))
    description = db.Column(db.Text, nullable=False)
    url_path = db.Column(db.String(63), index=True, nullable=False, unique=True)
    srd = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Creature ({self.name})>'
