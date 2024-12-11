"""DB creation

Revision ID: 188e79797577
Revises: 887cec43346a
Create Date: 2024-12-06 15:33:36.026553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '188e79797577'
down_revision: Union[str, None] = '887cec43346a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
