"""increase casting time column size

Revision ID: d40e31f7c5de
Revises: 0e8b5fcf6ceb
Create Date: 2021-12-16 07:02:40.665674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd40e31f7c5de'
down_revision = '0e8b5fcf6ceb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('spells', 'casting_time',
               existing_type=sa.VARCHAR(length=127),
               type_=sa.String(length=255),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('spells', 'casting_time',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=127),
               existing_nullable=False)
    # ### end Alembic commands ###
