from dataclasses import dataclass

from dbm_database_service.models.column import Column


@dataclass
class Table:
    name: str
    columns: list[Column]
    if_not_exist: bool = False
    temporary: bool = False

    def __str__(self) -> str:
        return f"create{' temporary' if self.temporary else ''} table" \
               f"{' if not exists' if self.if_not_exist else ''}" \
               f" {self.name}(" \
               f"{', '.join([str(c) for c in self.columns])});" \


    def drop_statement(self) -> str:
        return f"drop table if exists {self.name}"

    def alter_statement(self) -> str:
        return f"alter table {self.name}"

