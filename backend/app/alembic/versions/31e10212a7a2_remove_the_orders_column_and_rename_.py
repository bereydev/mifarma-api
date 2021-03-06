"""Remove the orders column and rename ordercontents in orders

Revision ID: 31e10212a7a2
Revises: 2d4e92995819
Create Date: 2021-08-01 18:07:06.410624

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '31e10212a7a2'
down_revision = '2d4e92995819'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_content', sa.Column('pharmacy_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.execute("UPDATE order_content SET pharmacy_id = ORD.pharmacy_id FROM order_content OI INNER JOIN orders ORD ON OI.order_id = ORD.id")
    op.add_column('order_content', sa.Column('order_date', sa.DateTime(), nullable=True))
    op.execute("UPDATE order_content SET order_date = ORD.order_date FROM order_content OI INNER JOIN orders ORD ON OI.order_id = ORD.id")
    op.add_column('order_content', sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.execute("UPDATE order_content SET user_id = ORD.user_id FROM order_content OI INNER JOIN orders ORD ON OI.order_id = ORD.id")
    op.drop_column('order_content', 'order_id')
    op.drop_table('orders')
    op.rename_table('order_content', 'orders')
    op.create_foreign_key(None, 'orders', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'orders', 'pharmacies', ['pharmacy_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_column('orders', 'product_id')
    op.drop_column('orders', 'order_id')
    op.drop_column('orders', 'delivery_date')
    op.drop_column('orders', 'amount')
    op.create_table('order_content',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('product_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('order_id', postgresql.UUID(), autoincrement=False, nullable=True),
    sa.Column('amount', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('delivery_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name='order_content_order_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='order_content_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='order_content_pkey')
    )
    op.create_index('ix_order_content_id', 'order_content', ['id'], unique=False)
    # ### end Alembic commands ###
