"""empty message

Revision ID: ff6f33628006
Revises: 5f171a73282a
Create Date: 2022-04-11 18:15:46.195835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff6f33628006'
down_revision = '5f171a73282a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('thankful_posts', sa.Column('title', sa.String(length=140), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('thankful_posts', 'title')
    # ### end Alembic commands ###
