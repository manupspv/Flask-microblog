"""new fields in user model

Revision ID: 84b2f1e94ed1
Revises: 1f99dc894757
Create Date: 2020-05-12 14:41:20.494557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84b2f1e94ed1'
down_revision = '1f99dc894757'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
