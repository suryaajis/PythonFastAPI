"""create table user

Revision ID: 6a572676735e
Revises: 
Create Date: 2024-03-31 21:50:51.327130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a572676735e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users", 
                    sa.Column("id", sa.INTEGER(), primary_key=True, nullable=False, index=True), 
                    sa.Column("email", sa.VARCHAR(), nullable=False, unique=True), 
                    sa.Column("username", sa.VARCHAR(), nullable=False), 
                    sa.Column("password", sa.VARCHAR(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
