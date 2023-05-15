"""Added Trucks table

Revision ID: 7cf2b28e7255
Revises: 
Create Date: 2023-05-15 19:29:07.188365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7cf2b28e7255"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "Trucks",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.column(
            "license_plate", sa.String(10), nullable=False, index=False, unique=True
        ),
        sa.Column("manufactured_by", sa.Integer, index=False, unique=False),
        sa.Column("model", sa.Integer, unique=False, index=False),
        sa.Column("year", sa.SmallInteger, unique=False, index=False),
        sa.Column("capacity", sa.Integer, unique=False, index=False),
        sa.Column("status", sa.Boolean, unique=False, index=False),
    )


def downgrade() -> None:
    op.drop_table("Trucks")
