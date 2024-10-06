"""add FK to posts tabe

Revision ID: e13ffbf6441c
Revises: 22760e5c50b4
Create Date: 2024-10-06 14:29:36.279696

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e13ffbf6441c'
down_revision: Union[str, None] = '22760e5c50b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_FK', source_table="posts", referent_table="users", 
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_FK', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
