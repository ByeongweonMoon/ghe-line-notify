"""empty message

Revision ID: dbf93173e596
Revises: None
Create Date: 2016-09-22 20:01:54.744330

"""

# revision identifiers, used by Alembic.
revision = 'dbf93173e596'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('template',
    sa.Column('token_id', sa.Integer(), nullable=False),
    sa.Column('event', sa.String(length=255), nullable=False),
    sa.Column('template', sa.String(length=1000), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('token_id', 'event')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=255), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('secret', sa.String(length=255), server_default='', nullable=False),
    sa.Column('description', sa.String(length=255), server_default='', nullable=False),
    sa.Column('tags', sa.String(length=255), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token')
    op.drop_table('template')
    ### end Alembic commands ###
