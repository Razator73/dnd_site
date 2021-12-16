"""Remove tags column from spells and creatures tables.

Revision ID: da2af3c53236
Revises: e1a30fabfa7f
Create Date: 2021-12-16 09:31:28.938017

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'da2af3c53236'
down_revision = 'e1a30fabfa7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('creature_tag_links', 'creature_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('creature_tag_links', 'creature_tag_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('creatures', 'tags')
    op.alter_column('spell_tag_links', 'spell_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('spell_tag_links', 'spell_tag_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('spells', 'tags')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spells', sa.Column('tags', postgresql.ARRAY(sa.VARCHAR(length=31)), autoincrement=False, nullable=False))
    op.alter_column('spell_tag_links', 'spell_tag_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('spell_tag_links', 'spell_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('creatures', sa.Column('tags', postgresql.ARRAY(sa.VARCHAR(length=63)), autoincrement=False, nullable=False))
    op.alter_column('creature_tag_links', 'creature_tag_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('creature_tag_links', 'creature_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###