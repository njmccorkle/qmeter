"""empty message

Revision ID: 485d5f7f9f54
Revises: 
Create Date: 2019-03-03 22:52:29.840156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '485d5f7f9f54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('session_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('setpoint', sa.Integer(), nullable=True),
    sa.Column('fan', sa.Integer(), nullable=True),
    sa.Column('temp0', sa.Numeric(precision=2), nullable=True),
    sa.Column('temp1', sa.Numeric(precision=2), nullable=True),
    sa.Column('temp2', sa.Numeric(precision=2), nullable=True),
    sa.Column('temp3', sa.Numeric(precision=2), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session_data')
    op.drop_table('sessions')
    # ### end Alembic commands ###
