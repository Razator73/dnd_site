"""Add characters and spellbooks tables

Revision ID: 50791727d1db
Revises: d76e0cd6ff80
Create Date: 2022-07-22 14:13:33.192446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50791727d1db'
down_revision = 'd76e0cd6ff80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('portrait_path', sa.String(length=127), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spellbooks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spellbook_spells',
    sa.Column('spell_id', sa.Integer(), nullable=False),
    sa.Column('spellbook_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['spell_id'], ['spells.id'], ),
    sa.ForeignKeyConstraint(['spellbook_id'], ['spellbooks.id'], ),
    sa.PrimaryKeyConstraint('spell_id', 'spellbook_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spellbook_spells')
    op.drop_table('spellbooks')
    op.drop_table('characters')
    # ### end Alembic commands ###
