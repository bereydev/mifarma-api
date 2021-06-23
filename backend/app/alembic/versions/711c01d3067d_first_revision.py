"""First revision

Revision ID: 711c01d3067d
Revises: 
Create Date: 2021-06-18 12:14:32.886677

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '711c01d3067d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('filename', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_images_id'), 'images', ['id'], unique=False)
    op.create_table('pharmacies',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('address2', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('schedule', sa.JSON(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pharmacies_id'), 'pharmacies', ['id'], unique=False)
    op.create_index(op.f('ix_pharmacies_name'), 'pharmacies', ['name'], unique=False)
    op.create_table('products',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('ean_code', sa.String(), nullable=False),
    sa.Column('classification_number', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('pharma_indications', sa.String(), nullable=True),
    sa.Column('type_of_material', sa.Integer(), nullable=True),
    sa.Column('magnitude', sa.Float(), nullable=True),
    sa.Column('laboratory', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_ean_code'), 'products', ['ean_code'], unique=False)
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=False)
    op.create_table('roles',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    op.create_table('drugs',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('with_prescription', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_drugs_id'), 'drugs', ['id'], unique=False)
    op.create_table('stock_items',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('pharmacy_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('product_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('name_unaccented', sa.String(), nullable=True),
    sa.Column('discount', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['pharmacies.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stock_items_id'), 'stock_items', ['id'], unique=False)
    op.create_index(op.f('ix_stock_items_name_unaccented'), 'stock_items', ['name_unaccented'], unique=False)
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('role_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('pregnant', sa.Boolean(), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('allergies', sa.JSON(), nullable=False),
    sa.Column('smoker', sa.Boolean(), nullable=True),
    sa.Column('addict', sa.Boolean(), nullable=True),
    sa.Column('alcoholic', sa.Boolean(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('postcode', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('prescriptions', sa.JSON(), nullable=False),
    sa.Column('previous_diseases', sa.JSON(), nullable=False),
    sa.Column('pharmacist_number', sa.String(), nullable=True),
    sa.Column('pharmacy_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('activated', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['pharmacies.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('orders',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('pharmacy_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['pharmacies.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=False)
    op.create_table('order_content',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('product_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('order_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('delivery_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_content_id'), 'order_content', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_content_id'), table_name='order_content')
    op.drop_table('order_content')
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_stock_items_name_unaccented'), table_name='stock_items')
    op.drop_index(op.f('ix_stock_items_id'), table_name='stock_items')
    op.drop_table('stock_items')
    op.drop_index(op.f('ix_drugs_id'), table_name='drugs')
    op.drop_table('drugs')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_index(op.f('ix_products_ean_code'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_pharmacies_name'), table_name='pharmacies')
    op.drop_index(op.f('ix_pharmacies_id'), table_name='pharmacies')
    op.drop_table('pharmacies')
    op.drop_index(op.f('ix_images_id'), table_name='images')
    op.drop_table('images')
    # ### end Alembic commands ###
