"""empty message

Revision ID: 0ec68ead18ef
Revises: 
Create Date: 2021-12-14 22:30:01.106471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ec68ead18ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Driver',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('registered_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_Driver_firstname'), 'Driver', ['firstname'], unique=False)
    op.create_index(op.f('ix_Driver_lastname'), 'Driver', ['lastname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Driver_lastname'), table_name='Driver')
    op.drop_index(op.f('ix_Driver_firstname'), table_name='Driver')
    op.drop_table('Driver')
    # ### end Alembic commands ###
