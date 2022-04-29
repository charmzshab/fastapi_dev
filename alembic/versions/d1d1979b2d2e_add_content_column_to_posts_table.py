"""add content column to posts table

Revision ID: d1d1979b2d2e
Revises: e43f824373e4
Create Date: 2022-04-29 09:10:30.728124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1d1979b2d2e'
down_revision = 'e43f824373e4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
