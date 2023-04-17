from dataclasses import dataclass
from dbm_database_service.models.config import Settings


@dataclass
class DataType:
    name: str
    corresponding_value: tuple | int = None

    def __post_init__(self) -> None:
        if self.name.upper() not in Settings.valid_mysql_datatypes:
            raise ValueError('Invalid datatype name')
        if self.corresponding_value is not None and self.name.upper() not in Settings.mysql_datatypes_with_corresponding_value:
            raise ValueError("Provided datatype shouldn't have corresponding value")

    def __str__(self) -> str:
        single_value = isinstance(self.corresponding_value, int)

        corresponding_value_str = "" if self.corresponding_value is None else \
            f"({self.corresponding_value if single_value else ', '.join([str(v) for v in self.corresponding_value])})"
        return f"{self.name}{corresponding_value_str}"
