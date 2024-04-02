"""add date table user

Revision ID: b7d0775d8766
Revises: 6a572676735e
Create Date: 2024-04-02 06:08:08.827943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b7d0775d8766'
down_revision: Union[str, None] = '6a572676735e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column("users", sa.Column('is_active', sa.BOOLEAN(), default=True, nullable=False))
    op.add_column("users", sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False))
    op.add_column("users", sa.Column('updated_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False, onupdate=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column("users", "is_active")
    op.drop_column("users", "created_at")
    op.drop_column("users", "updated_at")
    pass
