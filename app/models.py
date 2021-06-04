from sqlalchemy.dialects.postgresql import ARRAY

from app import db


class ModelCrud:
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


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

    def __repr__(self):
        return f'<Creature ({self.name})>'
