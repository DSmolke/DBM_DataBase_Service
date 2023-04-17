
import re

import pytest

from dbm_database_service.models.datatype import DataType


class TestValidCases:
    def test_with_valid_name(self, valid_mysql_datatypes) -> None:
        assert str(DataType(name=valid_mysql_datatypes)).upper() in [
            'INT', 'SMALLINT', 'TINYINT', 'MEDIUMINT',
            'BIGINT', 'ENUM',
            'BINARY', 'VARBINARY', 'BLOB',
            'DATE', 'TIME', 'DATETIME', 'TIMESTAMP',
            'YEAR', 'BOOLEAN', 'SET', 'JSON',
            'GEOMETRY', 'NULL', 'DECIMAL', 'FLOAT', 'DOUBLE',
            'CHAR', 'VARCHAR', 'TEXT'
        ]

    def test_with_valid_name_and_corresponding_value(self, valid_mysql_datatypes_with_corresponding_value) -> None:
        assert re.match(r'^[A-Za-z]+\(\d+(, \d+)?\)$', str(DataType(*valid_mysql_datatypes_with_corresponding_value)))

class TestInvalidCases:
    def test_with_invalid_name(self) -> None:
        with pytest.raises(ValueError) as e:
            DataType('dict')
        assert e.value.args[0] == 'Invalid datatype name'

    def test_with_invalid_corresponding_value(self) -> None:
        with pytest.raises(ValueError) as e:
            DataType('int', 1)
        assert e.value.args[0] == "Provided datatype shouldn't have corresponding value"
