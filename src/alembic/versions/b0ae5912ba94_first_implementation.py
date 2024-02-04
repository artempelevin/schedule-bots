"""first implementation

Revision ID: b0ae5912ba94
Revises: 
Create Date: 2024-02-04 13:40:38.172775

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b0ae5912ba94"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "university",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("short_name", sa.String(length=8), nullable=False),
        sa.Column("full_name", sa.String(length=256), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_university_full_name"), "university", ["full_name"], unique=True)
    op.create_index(op.f("ix_university_short_name"), "university", ["short_name"], unique=False)
    op.create_table(
        "institute",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("short_name", sa.String(length=8), nullable=False),
        sa.Column("full_name", sa.String(length=256), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("university_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["university_id"],
            ["university.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_institute_full_name"), "institute", ["full_name"], unique=True)
    op.create_index(op.f("ix_institute_short_name"), "institute", ["short_name"], unique=False)
    op.create_table(
        "group",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("short_name", sa.String(length=8), nullable=False),
        sa.Column("full_name", sa.String(length=64), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("course", sa.Enum("FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", name="course"), nullable=False),
        sa.Column("is_master_program", sa.Boolean(), server_default="0", nullable=False),
        sa.Column("institute_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["institute_id"],
            ["institute.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_group_full_name"), "group", ["full_name"], unique=True)
    op.create_index(op.f("ix_group_short_name"), "group", ["short_name"], unique=False)
    op.create_table(
        "schedule",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "day",
            sa.Enum("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", name="dayofweek"),
            nullable=False,
        ),
        sa.Column("start_time", sa.Time(), nullable=False),
        sa.Column("end_time", sa.Time(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("group_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["group_id"],
            ["group.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("schedule")
    op.drop_index(op.f("ix_group_short_name"), table_name="group")
    op.drop_index(op.f("ix_group_full_name"), table_name="group")
    op.drop_table("group")
    op.drop_index(op.f("ix_institute_short_name"), table_name="institute")
    op.drop_index(op.f("ix_institute_full_name"), table_name="institute")
    op.drop_table("institute")
    op.drop_index(op.f("ix_university_short_name"), table_name="university")
    op.drop_index(op.f("ix_university_full_name"), table_name="university")
    op.drop_table("university")
    # ### end Alembic commands ###
