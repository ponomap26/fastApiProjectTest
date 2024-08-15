"""add cat_id table product

Revision ID: c86c76ab563b
Revises: d6760d8a7140
Create Date: 2024-08-12 00:31:46.952048

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c86c76ab563b"
down_revision: Union[str, None] = "d6760d8a7140"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("price", sa.Integer(), nullable=True),
        sa.Column("cat_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["cat_id"],
            ["category.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("products")
    op.drop_column("category", "name")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("category", sa.Column("name", sa.VARCHAR(), nullable=False))
    op.create_table(
        "products",
        sa.Column("name", sa.VARCHAR(), nullable=False),
        sa.Column("description", sa.VARCHAR(), nullable=False),
        sa.Column("price", sa.INTEGER(), nullable=False),
        sa.Column("cat_id", sa.INTEGER(), nullable=False),
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(
            ["cat_id"],
            ["category.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("product")
    # ### end Alembic commands ###
