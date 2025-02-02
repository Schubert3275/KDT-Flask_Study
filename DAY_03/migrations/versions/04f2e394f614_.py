"""empty message

Revision ID: 04f2e394f614
Revises: 
Create Date: 2024-04-18 15:32:22.245842

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '04f2e394f614'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('favorite_food')
    op.drop_table('person')
    op.drop_table('string_tbl')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('string_tbl',
    sa.Column('char_fld', mysql.CHAR(collation='utf8mb4_unicode_ci', length=30), nullable=True),
    sa.Column('vchar_fld', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('text_fld', mysql.TEXT(collation='utf8mb4_unicode_ci'), nullable=True),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('person',
    sa.Column('person_id', mysql.SMALLINT(unsigned=True), autoincrement=True, nullable=False),
    sa.Column('fname', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=True),
    sa.Column('lname', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=True),
    sa.Column('eye_color', mysql.ENUM('BR', 'BL', 'GR'), nullable=True),
    sa.Column('birth_date', sa.DATE(), nullable=True),
    sa.Column('street', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=30), nullable=True),
    sa.Column('city', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=True),
    sa.Column('state', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=True),
    sa.Column('contry', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=True),
    sa.Column('postal_code', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=True),
    sa.PrimaryKeyConstraint('person_id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('favorite_food',
    sa.Column('person_id', mysql.SMALLINT(unsigned=True), autoincrement=False, nullable=False),
    sa.Column('food', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.person_id'], name='fk_fav_food_person_id'),
    sa.PrimaryKeyConstraint('person_id', 'food'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('answer')
    op.drop_table('question')
    # ### end Alembic commands ###
