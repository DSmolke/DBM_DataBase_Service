import pytest

from dbm_database_service.connectors import get_connection_pool
from dbm_database_service.managers import MySQLDatabaseManager
from dbm_database_service.models.column import Column
from dbm_database_service.models.datatype import DataType
from dbm_database_service.models.table import Table


class TestValidCases:
    @pytest.mark.xfail(message="Table 'cars' already exists")
    def test_valid_create_table(self) -> None:
        """
        If we run test first time, there is no table cars in db and call doesn't
        raise an error
        """
        with pytest.raises(Exception) as e:
            mng = MySQLDatabaseManager(get_connection_pool())
            mng.create_table(Table('cars', [Column('id', datatype=DataType('int'))]))
        assert e.value.args[0] == 1050
