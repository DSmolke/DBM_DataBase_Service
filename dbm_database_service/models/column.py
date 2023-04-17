from dataclasses import dataclass
from typing import Any

from dbm_database_service.models.datatype import DataType
from easyvalid_data_validator.validator import validate_json_data
from easyvalid_data_validator.constraints import Constraint


@dataclass
class Column:
    """ Needs minimum of name and datatype to parse and can be extended by primary key, autoincrement, unique, default, not_null"""
    name: str
    datatype: DataType
    primary_key: bool = False
    autoincrement: bool = False
    unique: bool = False
    default: Any = None
    not_null: bool = False

    def __post_init__(self) -> None:
        """ Validates if provided arguments are valid """
        namespaces = self.__dict__
        constraints = {
            "name": {Constraint.STRING_REGEX: r'^[a-zA-Z_][a-zA-Z0-9_]{1,64}$'},
            "primary_key": {Constraint.IS_TYPE: bool},
            "autoincrement": {Constraint.IS_TYPE: bool},
            "unique": {Constraint.IS_TYPE: bool},
            "not_null": {Constraint.IS_TYPE: bool}
        }
        validate_json_data(namespaces, constraints)

    def __str__(self):
        """ Will be parsed in other objects. Outcome is valid sql string describing column """
        return f"{self.name} {self.datatype}" \
               f"{' primary key' if self.primary_key else ''}" \
               f"{' autoincrement' if self.autoincrement else ''}" \
               f"{' unique' if self.unique else ''}" \
               f"{' not null' if self.not_null else ''}" \
               f"{f' default {self.default}' if self.default else ''}"
