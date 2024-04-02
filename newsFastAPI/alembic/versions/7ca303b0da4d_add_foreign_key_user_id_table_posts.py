"""add foreign key user_id table posts


Revision ID: 7ca303b0da4d
Revises: a8ca5bd73f12
Create Date: 2024-04-02 06:26:08.850089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ca303b0da4d'
down_revision: Union[str, None] = 'a8ca5bd73f12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("user_id", sa.INTEGER(), nullable=False))
    op.create_foreign_key("posts_user_id_fk", source_table="posts", referent_table="users", local_cols=["user_id"], remote_cols=["id"], ondelete="CASCADE", onupdate="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "user_id")
    pass
