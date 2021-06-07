"""users table

Revision ID: 435d8affeb4e
Revises: a970f029c533
Create Date: 2021-06-05 10:36:20.850022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '435d8affeb4e'
down_revision = 'a970f029c533'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=63), nullable=False),
    sa.Column('email', sa.String(length=127), nullable=False),
    sa.Column('password_hash', sa.String(length=127), nullable=False),
    sa.Column('role', sa.String(length=15), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
