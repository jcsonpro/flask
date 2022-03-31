"""empty message

Revision ID: 9d3957d24753
Revises: a5e2d7b2ab61
Create Date: 2022-03-31 11:55:33.485487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d3957d24753'
down_revision = 'a5e2d7b2ab61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_user_email'), type_='unique')

    # ### end Alembic commands ###