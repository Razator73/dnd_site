"""srd col constraints

Revision ID: a970f029c533
Revises: 0cb6bd1bc1a9
Create Date: 2021-06-04 10:28:52.699599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a970f029c533'
down_revision = '0cb6bd1bc1a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('creatures', 'srd',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('spells', 'srd',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('spells', 'srd',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('creatures', 'srd',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
