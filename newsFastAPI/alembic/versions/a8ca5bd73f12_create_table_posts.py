"""create table posts

Revision ID: a8ca5bd73f12
Revises: b7d0775d8766
Create Date: 2024-04-02 06:16:21.026285

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8ca5bd73f12'
down_revision: Union[str, None] = 'b7d0775d8766'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', 
                    sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True), 
                    sa.Column('title', sa.VARCHAR(), nullable=False), 
                    sa.Column('content', sa.VARCHAR(), nullable=False),  
                    sa.Column('published', sa.VARCHAR(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False, onupdate=sa.text('now()'))
                    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
