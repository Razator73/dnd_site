"""Add tag_str column for creatures and spells

Revision ID: d76e0cd6ff80
Revises: da2af3c53236
Create Date: 2021-12-16 10:58:18.098162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd76e0cd6ff80'
down_revision = 'da2af3c53236'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('creatures', sa.Column('tag_str', sa.String(length=255), nullable=True))
    op.add_column('spells', sa.Column('tag_str', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('spells', 'tag_str')
    op.drop_column('creatures', 'tag_str')
    # ### end Alembic commands ###
