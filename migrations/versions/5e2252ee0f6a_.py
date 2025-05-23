"""empty message

Revision ID: 5e2252ee0f6a
Revises: a71bf5ecceff
Create Date: 2025-04-25 18:12:39.330132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e2252ee0f6a'
down_revision = 'a71bf5ecceff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('personajes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planeta_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'planetas', ['planeta_id'], ['planeta_id'])

    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('personaje_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'personajes', ['personaje_id'], ['personaje_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('personaje_id')

    with op.batch_alter_table('personajes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('planeta_id')

    # ### end Alembic commands ###
