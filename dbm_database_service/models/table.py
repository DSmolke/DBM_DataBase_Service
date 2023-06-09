from dataclasses import dataclass

from dbm_database_service.models.column import Column


@dataclass
class Table:
    name: str
    columns: list[Column]
    if_not_exist: bool = False
    temporary: bool = False

    def __str__(self) -> str:
        """ Will be parsed in other objects. Outcome is valid SQL Create Table expression """
        return f"create{' temporary' if self.temporary else ''} table{' if not exists' if self.if_not_exist else ''} {self.name}({', '.join([str(c) for c in self.columns])});"

    def drop_statement(self) -> str:
        """ Auxiliary method, that returns expression of sql drop table if exist with name stored in instance """
        return f"drop table if exists {self.name}"

    def alter_statement(self) -> str:
        """ Auxiliary method, that returns expression of sql alter table with name stored in instance """
        return f"alter table {self.name}"

