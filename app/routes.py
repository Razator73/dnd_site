import markdown
from flask import render_template

from app import app
from app.models import Spell, Creature


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


@app.template_filter()
def number_format(value):
    return f'{value:,}'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/spells')
def spell_home():
    spells = Spell.query.order_by(Spell.level, Spell.name).all()
    spells_by_level = group_spells(spells)
    schools = set([s.school for s in spells])
    return render_template('spell_home.html', title='Spells', spell_lists=spells_by_level, schools=schools)


@app.route('/spells/<spell_name>')
def spell_page(spell_name):
    spell = Spell.query.filter_by(url_path=spell_name).first_or_404()
    return render_template('spell_page.html', title=spell.name, spell=spell, markdown=markdown.markdown)


@app.route('/spells/tags/<tag_name>')
def spells_by_tag(tag_name):
    tag_spells = Spell.query.filter(Spell.tags.contains([tag_name])).order_by(Spell.level, Spell.name).all()
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
