"""add content column to posts table

Revision ID: 714fcd34b866
Revises: 4b2213d91547
Create Date: 2024-10-06 00:37:50.892036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '714fcd34b866'
down_revision: Union[str, None] = '4b2213d91547'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
