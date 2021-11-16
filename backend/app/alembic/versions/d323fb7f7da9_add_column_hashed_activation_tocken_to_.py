"""Add column hashed_activation_tocken to Table user

Revision ID: d323fb7f7da9
Revises: 2cbf1b81bde7
Create Date: 2021-11-15 14:50:13.570975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd323fb7f7da9'
down_revision = '2cbf1b81bde7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_activation_token', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'hashed_activation_token')
    # ### end Alembic commands ###