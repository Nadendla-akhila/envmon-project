"""create sensor_readings table

Revision ID: 0001_create_sensor_readings
Revises: 
Create Date: 2025-09-14 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_create_sensor_readings'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'sensor_readings',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('sensor_id', sa.String(), nullable=False),
        sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
        sa.Column('pm25', sa.Float(), nullable=True),
        sa.Column('pm10', sa.Float(), nullable=True),
        sa.Column('no2', sa.Float(), nullable=True),
        sa.Column('so2', sa.Float(), nullable=True),
        sa.Column('o3', sa.Float(), nullable=True),
        sa.Column('co', sa.Float(), nullable=True),
        sa.Column('temperature', sa.Float(), nullable=True),
        sa.Column('humidity', sa.Float(), nullable=True),
    )

def downgrade():
    op.drop_table('sensor_readings')
