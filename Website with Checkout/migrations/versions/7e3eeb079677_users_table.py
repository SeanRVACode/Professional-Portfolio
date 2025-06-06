"""users table

Revision ID: 7e3eeb079677
Revises: 
Create Date: 2025-04-24 10:16:34.420128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e3eeb079677'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('address_line1', sa.String(length=128), nullable=True),
    sa.Column('address_line2', sa.String(length=128), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=64), nullable=True),
    sa.Column('postal_code', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
