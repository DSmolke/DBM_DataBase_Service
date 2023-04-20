from dbm_database_service.models.column import Column
from dbm_database_service.models.datatype import DataType
from dbm_database_service.models.table import Table


class TestValidCases:
    def test_with_valid_name_and_column(self, valid_table_name, valid_table_columns) -> None:
        assert str(Table(valid_table_name, valid_table_columns)) == \
               "create table cars(id int primary key auto_increment, name varchar(10));"

    def test_with_if_not_exists(self, valid_table_name, valid_table_columns) -> None:
        assert str(Table(valid_table_name, valid_table_columns, if_not_exist=True)) == \
               "create table if not exists cars(id int primary key auto_increment, name varchar(10));"

    def test_with_temporary(self, valid_table_name, valid_table_columns) -> None:
        assert str(Table(valid_table_name, valid_table_columns, temporary=True)) == \
               "create temporary table cars(id int primary key auto_increment, name varchar(10));"

    def test_with_multiple_columns_with_primary_key_and_auto_increments(self) -> None:
        columns = [
            Column('id', DataType('int'), primary_key=True, auto_increment=True),
            Column('name', DataType('varchar', 255)),
            Column('points', DataType('int'))
        ]
        table = Table('teams', columns=columns)
        assert str(table) == 'create table teams(id int primary key auto_increment, name varchar(255), points int);'
        assert type(str(table)) == str
