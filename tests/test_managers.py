import pytest

from dbm_database_service.connectors import get_connection_pool
from dbm_database_service.managers import MySQLDatabaseManager
from dbm_database_service.models.column import Column
from dbm_database_service.models.datatype import DataType
from dbm_database_service.models.table import Table


class TestValidCases:
    def test_create_table_valid_create_table(self) -> None:
        """
        If we run test first time, there is no table cars in db and call doesn't
        raise an error
        """
        mng = MySQLDatabaseManager(get_connection_pool())
        mng.drop_table_if_exists('cars')
        mng.create_table(Table('cars', [Column('id', datatype=DataType('int'))]))
        mng.dev_console('insert into cars (id) value (null)')
        assert mng.dev_console('select * from cars') == [(None,)]

    def test_drop_table_if_exists_with_valid_string(self) -> None:
        mng = MySQLDatabaseManager(get_connection_pool())
        mng.create_table(Table('cars', [Column('id', datatype=DataType('int'))]))
        mng.drop_table_if_exists('cars')
        assert mng.dev_console('select * from cars') is None

    def test_drop_table_if_exists_with_valid_table(self) -> None:
        mng = MySQLDatabaseManager(get_connection_pool())
        t = Table('cars', [Column('id', datatype=DataType('int'))])
        mng.create_table(t)
        mng.drop_table_if_exists(t)
        assert mng.dev_console('select * from cars') is None

    def test_add_columns_with_valid_args(self) -> None:
        mng = MySQLDatabaseManager(get_connection_pool())
        mng.drop_table_if_exists('cars')
        t = Table('cars', [Column('id', datatype=DataType('int'))])
        mng.create_table(t)
        mng.add_columns(t, columns=[
            Column('name', DataType('varchar', 200)),
            Column('age', DataType('int'))
        ])
        mng.dev_console('insert into cars (id, name, age) values (null, null, null)')
        assert mng.dev_console('select * from cars') == [(None, None, None)]


class TestInvalidCases:
    def test_create_table_with_invalid_argument(self):
        with pytest.raises(ValueError) as e:
            mng = MySQLDatabaseManager(get_connection_pool())
            mng.create_table('Some fake table')
        assert e.value.args[0] == 'Provided argument has to be Table object'
        assert e.type == ValueError

    def test_drop_table_if_exists_with_invalid_argument(self) -> None:
        with pytest.raises(ValueError) as e:
            mng = MySQLDatabaseManager(get_connection_pool())
            mng.drop_table_if_exists(1)
        assert e.value.args[0] == f'Provided argument has to be Table object'
        assert e.type == ValueError

    def test_add_columns_with_invalid_table(self) -> None:
        with pytest.raises(ValueError) as e:
            mng = MySQLDatabaseManager(get_connection_pool())
            mng.add_columns(table=1, columns=[
                Column('name', DataType('varchar', 200)),
                Column('age', DataType('int'))
            ])
        assert e.value.args[0] == 'Provided argument has to be Table object'
        assert e.type == ValueError

    def test_add_columns_with_invalid_columns(self) -> None:
        with pytest.raises(ValueError) as e:
            mng = MySQLDatabaseManager(get_connection_pool())
            mng.add_columns(table='cars', columns=[
                'col1', 'col2'
            ])
        assert e.value.args[0] == "Some values in 'columns' argument are not Column instances"
        assert e.type == ValueError
