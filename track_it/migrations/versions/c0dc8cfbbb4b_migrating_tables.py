"""Migrating tables

Revision ID: c0dc8cfbbb4b
Revises: 
Create Date: 2023-05-16 11:06:07.033954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c0dc8cfbbb4b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "trucks",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.Column("license_plate", sa.String(10), unique=True, index=False),
        sa.Column("manufactured_by", sa.String, index=False, unique=False),
        sa.Column("model", sa.Integer, unique=False, index=False),
        sa.Column("year", sa.SmallInteger, unique=False, index=False),
        sa.Column("capacity", sa.Integer, unique=False, index=False),
        sa.Column("status", sa.Boolean, unique=False, index=False),
    )

    op.create_table(
        "drivers",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("name", sa.String, unique=False, index=False),
        sa.Column("license_number", sa.String, unique=False, index=False),
        sa.Column("address", sa.String, unique=False, index=False),
        sa.Column("city", sa.String, index=False, unique=False),
        sa.Column("state", sa.String, index=False, unique=False),
        sa.Column("zipcode", sa.Integer, index=False, unique=False),
        sa.Column("phone_no", sa.Integer, unique=True, index=False),
        sa.Column("email", sa.String, unique=True, index=False),
        sa.Column("truck_id", sa.Integer, sa.ForeignKey("trucks.id")),
    )

    op.create_table(
        "shippers",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("name", sa.String, unique=False, index=False),
        sa.Column("address", sa.String, unique=False, index=False),
        sa.Column("cities", sa.String, index=False, unique=False),
        sa.Column("state", sa.String, index=False, unique=False),
        sa.Column("zipcode", sa.Integer, index=False, unique=False),
        sa.Column("phone_no", sa.Integer, unique=True, index=False),
        sa.Column("email", sa.String, unique=True, index=False),
    )

    op.create_table(
        "shipments",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("shipment_Date", sa.DateTime, index=False, unique=False),
        sa.Column("origin", sa.String, index=False, unique=False),
        sa.Column("destination", sa.String, index=False, unique=False),
        sa.Column("truck_id", sa.Integer, sa.ForeignKey("trucks.id")),
        sa.Column("driver_id", sa.Integer, sa.ForeignKey("drivers.id")),
        sa.Column("shipper_id", sa.Integer, sa.ForeignKey("shippers.id")),
        sa.Column("date", sa.Date, index=False, unique=False),
    )

    op.create_table(
        "goods",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("name", sa.String, unique=False, index=False),
        sa.Column("description", sa.String, unique=False, index=False),
        sa.Column("quantity", sa.Integer, unique=False, index=False),
        sa.Column("weights", sa.Integer, unique=False, index=False),
        sa.Column("value", sa.Integer, index=False, unique=False),
        sa.Column("shipments_id", sa.Integer, sa.ForeignKey("shipments.id")),
    )


def downgrade():
    op.drop_constraint("goods_shipments_id_fkey", "goods", type_="foreignkey")
    op.drop_constraint("shipments_truck_id_fkey", "shipments", type_="foreignkey")
    op.drop_constraint("shipments_driver_id_fkey", "shipments", type_="foreignkey")
    op.drop_constraint("shipments_shipper_id_fkey", "shipments", type_="foreignkey")
    op.drop_table("goods")
    op.drop_table("shipments")
    op.drop_table("shippers")
    op.drop_table("drivers")
    op.drop_table("trucks")
