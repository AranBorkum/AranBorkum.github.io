"""adding strike info table

Revision ID: a06af6938569
Revises: d640e70597dc
Create Date: 2023-01-02 12:09:48.167945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a06af6938569"
down_revision = "d640e70597dc"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "strike_info",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("date_of_strike", sa.Date(), nullable=True),
        sa.Column("strike_message", sa.String(), nullable=True),
        sa.Column(
            "date_added_to_db",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("strike_info")
    # ### end Alembic commands ###