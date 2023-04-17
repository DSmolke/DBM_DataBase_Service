from dbm_database_service.models.table import Table


class TestValidCases:
    def test_with_valid_name_and_column(self, valid_table_name, valid_table_columns) -> None:
        assert str(Table(valid_table_name, valid_table_columns)) == \
               "create table cars(id int primary key autoincrement, name varchar(10));"

    def test_with_if_not_exists(self, valid_table_name, valid_table_columns) -> None:
        assert str(Table(valid_table_name, valid_table_columns, if_not_exist=True)) == \
               "create table if not exists cars(id int primary key autoincrement, name varchar(10));"

    def test_with_temporary(self, valid_table_name, valid_table_columns) -> None:
        assert str(Table(valid_table_name, valid_table_columns, temporary=True)) == \
               "create temporary table cars(id int primary key autoincrement, name varchar(10));"
