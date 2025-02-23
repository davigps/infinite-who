"""create translation tables

Revision ID: af647043e0e5
Revises: 83e1d56e1af7
Create Date: 2025-02-23 18:32:59.970924

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "af647043e0e5"
down_revision: Union[str, None] = "83e1d56e1af7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "languages",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.String(length=5), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )
    op.create_table(
        "card_translations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("card_id", sa.Integer(), nullable=False),
        sa.Column("language_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["card_id"],
            ["cards.id"],
        ),
        sa.ForeignKeyConstraint(
            ["language_id"],
            ["languages.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "spoiler_translations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("spoiler_id", sa.Integer(), nullable=False),
        sa.Column("language_id", sa.Integer(), nullable=False),
        sa.Column("content", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["language_id"],
            ["languages.id"],
        ),
        sa.ForeignKeyConstraint(
            ["spoiler_id"],
            ["spoilers.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_column("cards", "title")
    op.drop_column("cards", "description")
    op.drop_column("spoilers", "content")
    # ### end Alembic commands ###

    # Insert default languages
    op.execute(
        """
        INSERT INTO languages (id, code, name, created_at, updated_at)
        VALUES
            (1, 'en', 'English', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
            (2, 'pt-BR', 'Portuguese (Brazil)', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        """
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "spoilers",
        sa.Column("content", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "cards",
        sa.Column("description", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "cards", sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=False)
    )
    op.drop_table("spoiler_translations")
    op.drop_table("card_translations")
    op.drop_table("languages")
    # ### end Alembic commands ###
