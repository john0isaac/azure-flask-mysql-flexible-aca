"""empty message

Revision ID: bdb17ae99c7e
Revises: 8f6c214ddf1b
Create Date: 2023-08-17 12:53:41.857926

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "bdb17ae99c7e"
down_revision = "8f6c214ddf1b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("cruise", schema=None) as batch_op:
        batch_op.alter_column(
            "description",
            existing_type=sa.VARCHAR(length=255),
            type_=sa.String(length=1000),
            existing_nullable=True,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("cruise", schema=None) as batch_op:
        batch_op.alter_column(
            "description",
            existing_type=sa.String(length=1000),
            type_=sa.VARCHAR(length=255),
            existing_nullable=True,
        )

    # ### end Alembic commands ###
