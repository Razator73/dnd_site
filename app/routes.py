import datetime as dt
import markdown

from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import app
from app.forms import LoginForm, RegistrationForm
from app.models import Spell, Creature, User


def group_spells(spells):
    grouped_spells = {}
    for spell in spells:
        key = f'Level {spell.level}' if spell.level > 0 else 'Cantrips'
        grouped_spells.setdefault(key, [])
        grouped_spells[key].append(spell)
    return grouped_spells


def group_creatures(creatures, byname=False):
    grouped_creatures = {}
    for creature in creatures:
        key = creature.name[0] if byname else creature.cr_string
        grouped_creatures.setdefault(key, [])
        grouped_creatures[key].append(creature)
    return grouped_creatures


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = dt.datetime.utcnow()


@app.template_filter()
def number_format(value):
    return f'{value:,}'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=login_form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=login_form)


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have logged out.')
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in. Please logout to create a new account.')
        return redirect(url_for('home'))
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        user = User(reg_form.username.data, reg_form.email.data, reg_form.password.data)
        user.save()
        flash('Thanks for registering!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=reg_form)


@app.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', title=user.username, user=user)


@app.route('/users')
def user_list():
    if current_user.is_authenticated and current_user.role_id == app.config.get('ADMIN_ROLE'):
        users = User.query.all()
        return render_template('users.html', title='Users', users=users)
    else:
        abort(404)


@app.route('/spells')
def spell_home():
    if current_user.is_authenticated and current_user.role_id > app.config.get('NON_SRD_ROLES'):
        spells = Spell.query.order_by(Spell.level, Spell.name).all()
    else:
        spells = Spell.query.filter_by(srd=True).order_by(Spell.level, Spell.name).all()
    spells_by_level = group_spells(spells)
    schools = set([s.school for s in spells])
    return render_template('spell_home.html', title='Spells', spell_lists=spells_by_level, schools=schools)


@app.route('/spells/<spell_name>')
def spell_page(spell_name):
    if current_user.is_authenticated and current_user.role_id > app.config['NON_SRD_ROLES']:
        spell = Spell.query.filter_by(url_path=spell_name).first_or_404()
    else:
        spell = Spell.query.filter_by(url_path=spell_name, srd=True).first_or_404()
    return render_template('spell_page.html', title=spell.name, spell=spell, markdown=markdown.markdown)


@app.route('/spells/tags/<tag_name>')
def spells_by_tag(tag_name):
    if current_user.is_authenticated and current_user.role_id > app.config['NON_SRD_ROLES']:
        tag_spells = Spell.query.filter(Spell.tags.contains([tag_name])).order_by(Spell.level, Spell.name).all()
    else:
        spells_filter = Spell.query.filter(Spell.tags.contains([tag_name]) & Spell.srd)
        tag_spells = spells_filter.order_by(Spell.level, Spell.name).all()
    grouped_tags = group_spells(tag_spells)
    schools = set([s.school for s in tag_spells])
    return render_template('spell_home.html', title=f'{tag_name.capitalize()} Spells',
                           spell_lists=grouped_tags, schools=schools)


@app.route('/creatures')
def creatures_home():
    creatures = Creature.query.order_by(Creature.cr, Creature.name).all()
    grouped_creatures = group_creatures(creatures)
    kinds = set([c.kind for c in creatures])
    return render_template('creature_home.html', title='Bestiary', grouped_creatures=grouped_creatures,
                           byname=False, kinds=kinds)


@app.route('/creatures/byname')
def creatures_by_name():
    creatures = Creature.query.order_by(Creature.name).all()
    grouped_creatures = group_creatures(creatures, byname=True)
    kinds = set([c.kind for c in creatures])
    return render_template('creature_home.html', title='Bestiary', grouped_creatures=grouped_creatures,
                           byname=True, kinds=kinds)


@app.route('/creatures/<creature_name>')
def creature_page(creature_name):
    creature = Creature.query.filter_by(url_path=creature_name).first_or_404()
    return render_template('creature_page.html', title=creature.name, creature=creature, markdown=markdown.markdown)


@app.route('/creatures/tags/<tag_name>')
def creatures_by_tag(tag_name):
    tag_creatures = Creature.query.filter(Creature.tags.contains([tag_name])).order_by(Creature.cr, Creature.name).all()
    grouped_creatures = group_creatures(tag_creatures)
    tag_name = tag_name.upper() if tag_name.startswith('cr') else tag_name.replace('-', ' ').title()
    kinds = set([c.kind for c in tag_creatures])
    return render_template('creature_home.html', title=f'{tag_name} Creatures',
                           grouped_creatures=grouped_creatures, kinds=kinds)