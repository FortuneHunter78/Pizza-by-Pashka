"""Create new string

Revision ID: 4d51e24a656d
Revises: 5aa59ddad436
Create Date: 2024-05-05 18:54:54.748591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d51e24a656d'
down_revision = '5aa59ddad436'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('birthDate', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('birthDate')

    # ### end Alembic commands ###
