"""remove description html

Revision ID: 934d52b4b803
Revises: af7fb4c6c12f
Create Date: 2021-06-01 16:01:56.847243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '934d52b4b803'
down_revision = 'af7fb4c6c12f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('creatures', 'description_html')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('creatures', sa.Column('description_html', sa.TEXT(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
