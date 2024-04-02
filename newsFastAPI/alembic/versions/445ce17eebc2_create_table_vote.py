"""create table vote'


Revision ID: 445ce17eebc2
Revises: 7ca303b0da4d
Create Date: 2024-04-02 10:13:16.873033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '445ce17eebc2'
down_revision: Union[str, None] = '7ca303b0da4d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("votes", 
                    sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True), 
                    sa.Column('user_id', sa.INTEGER(), nullable=False),
                    sa.Column('post_id', sa.INTEGER(), nullable=False), 
                    sa.Column('is_voted', sa.BOOLEAN(), default=False, nullable=False), 
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False, onupdate=sa.text('now()'))
                    )
    op.create_foreign_key("votes_user_id_fk", source_table="votes", referent_table="users", local_cols=["user_id"], remote_cols=["id"])
    op.create_foreign_key("votes_post_id_fk", source_table="votes", referent_table="posts", local_cols=["post_id"], remote_cols=["id"])
    pass


def downgrade() -> None:
    op.drop_table("votes")
    pass
