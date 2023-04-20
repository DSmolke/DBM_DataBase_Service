import pytest
from dbm_database_service.models.column import Column
from easyvalid_data_validator.customexceptions.common import ValidationError

class TestValidColumnCases:
    basic_name = 'id'

    def test_basic_colum(self, datatype_mock) -> None:
        """ Column with name and datatype"""
        assert str(Column(name=self.basic_name, datatype=datatype_mock)) == 'id int'

    def test_basic_column_with_primary_key(self, datatype_mock) -> None:
        assert str(Column(name=self.basic_name, datatype=datatype_mock, primary_key=True)) == 'id int primary key'

    def test_basic_column_with_autoincrement(self, datatype_mock) -> None:
        assert str(Column(name=self.basic_name, datatype=datatype_mock, auto_increment=True)) == 'id int auto_increment'

    def test_basic_column_with_unique(self, datatype_mock) -> None:
        assert str(Column(name=self.basic_name, datatype=datatype_mock, unique=True)) == 'id int unique'

    def test_basic_column_with_default(self, datatype_mock) -> None:
        assert str(Column(name=self.basic_name, datatype=datatype_mock, default=1)) == 'id int default 1'

    def test_basic_column_with_not_null(self, datatype_mock) -> None:
        assert str(Column(name=self.basic_name, datatype=datatype_mock, not_null=True)) == 'id int not null'

    def test_basic_column_with_autoincrement_and_primary_key(self, datatype_mock) -> None:
        assert str(Column(name=self.basic_name, datatype=datatype_mock, primary_key=True, auto_increment=True)) == 'id int primary key auto_increment'


class TestInvalidColumnCases:
    def test_with_invalid_names(self, invalid_column_names, datatype_mock) -> None:
        with pytest.raises(ValidationError) as e:
            Column(invalid_column_names, datatype=datatype_mock)
        assert e.value.args[0] == {'name': ['Invalid string expression - does not match regex']}

    def test_with_invalid_primary_keys(self, invalid_primary_key_values, datatype_mock) -> None:
        with pytest.raises(ValidationError) as e:
            Column('name', primary_key=invalid_primary_key_values, datatype=datatype_mock)
        assert e.value.args[0] == {'primary_key': ["Invalid type - isn't same type like compare type"]}

    def test_with_invalid_autoincrement(self, invalid_primary_key_values, datatype_mock) -> None:
        with pytest.raises(ValidationError) as e:
            Column('name', primary_key=invalid_primary_key_values, datatype=datatype_mock)
        assert e.value.args[0] == {'primary_key': ["Invalid type - isn't same type like compare type"]}

    def test_with_invalid_unique(self, invalid_unique_values, datatype_mock) -> None:
        with pytest.raises(ValidationError) as e:
            Column('name', unique=invalid_unique_values, datatype=datatype_mock)
        assert e.value.args[0] == {'unique': ["Invalid type - isn't same type like compare type"]}

    def test_with_invalid_not_null(self, invalid_not_null_values, datatype_mock) -> None:
        with pytest.raises(ValidationError) as e:
            Column('name', not_null=invalid_not_null_values, datatype=datatype_mock)
        assert e.value.args[0] == {'not_null': ["Invalid type - isn't same type like compare type"]}

