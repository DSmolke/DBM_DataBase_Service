import pytest
from unittest.mock import MagicMock

from dbm_database_service.models.column import Column
from dbm_database_service.models.datatype import DataType


@pytest.fixture
def datatype_mock():
    datatype_mock = MagicMock()
    datatype_mock.__str__.return_value = 'int'
    return datatype_mock


@pytest.fixture(params=[
    'to_long____________________________________________________________________',
    '1_cars'
])
def invalid_column_names(request):
    return request.param

@pytest.fixture(params=[
    1, '2', (True, )
])
def invalid_primary_key_values(request):
    return request.param

@pytest.fixture(params=[
    1, '2', (True, )
])
def invalid_autoincrement_values(request):
    return request.param

@pytest.fixture(params=[
    1, '2', (True, )
])
def invalid_unique_values(request):
    return request.param

@pytest.fixture(params=[
    1, '2', (True, )
])
def invalid_not_null_values(request):
    return request.param


@pytest.fixture(params=[
    'INT', 'SMALLINT', 'TINYINT', 'MEDIUMINT',
    'BIGINT', 'ENUM',
    'BINARY', 'VARBINARY', 'BLOB',
    'DATE', 'TIME', 'DATETIME', 'TIMESTAMP',
    'YEAR', 'BOOLEAN', 'SET', 'JSON',
    'GEOMETRY', 'NULL'])
def valid_mysql_datatypes(request):
    return request.param

@pytest.fixture(params=[
    ('DECIMAL', (2, 2)), ('FLOAT', (2, 2)), ('DOUBLE', (2, 2)),
    ('CHAR', 2), ('VARCHAR', 2), ('TEXT', 2)
    ])
def valid_mysql_datatypes_with_corresponding_value(request):
    return request.param

@pytest.fixture
def valid_table_name():
    return 'cars'

@pytest.fixture
def valid_table_columns():
    return [
        Column('id', DataType('int'), primary_key=True, auto_increment=True),
        Column('name', DataType('varchar', 10))
    ]
