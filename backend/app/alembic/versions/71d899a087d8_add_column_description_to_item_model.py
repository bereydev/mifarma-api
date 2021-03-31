"""Add column description to Item model

Revision ID: 71d899a087d8
Revises: d4867f3a4c0a
Create Date: 2021-03-15 02:52:49.922490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71d899a087d8'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
