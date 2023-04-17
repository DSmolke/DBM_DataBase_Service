from contextlib import contextmanager
from mysql.connector import Error

from dbm_database_service.models.column import Column
from dbm_database_service.models.table import Table


class MySQLDatabaseManager:
    def __init__(self, connection_pool) -> None:
        self._connection_pool = connection_pool

    @contextmanager
    def _get_cursor_object(self):
        """ Custom context manager for db cursor. Uses object's connection pool to establish connection and later on cursor """
        connection_object = self._connection_pool.get_connection()
        try:
            if connection_object.is_connected():
                cursor_object = connection_object.cursor()
                yield cursor_object
                connection_object.commit()
        except Error as e:
            connection_object.rollback()
        finally:
            if connection_object.is_connected():
                cursor_object.close()
                connection_object.close()

    def create_table(self, table: Table) -> None:
        """
        Creates table in database using Table instance as a provider of specification of the table
        :param table: Table instance
        :return: None
        """
        if not isinstance(table, Table):
            raise ValueError(f'Provided argument has to be Table object')
        with self._get_cursor_object() as cur:
            cur.execute(str(table))

    def drop_table_if_exists(self, table: str | Table) -> None:
        """
        Drops a table if any exists in database. Does not cause error as long as connection is valid
        :param table: table name or Table instance
        :return: None
        """
        with self._get_cursor_object() as cur:
            if type(table) == str:
                cur.execute(f"drop table if exists {table}")
            elif isinstance(table, Table):
                cur.execute(table.drop_statement())
            else:
                raise ValueError(f'Provided argument has to be Table object')

    def add_columns(self, table: str | Table, columns: list[Column]) -> None:
        """
        Ads columns into existing table. Can work on one or more Columns
        :param table: table name or Table instance
        :param columns: list of Column instances
        :return: None
        """
        if not all([True if isinstance(c, Column) else False for c in columns]):
            raise ValueError("Some values in 'columns' argument are not Column instances")
        add_statement = ", ".join([f"add column {str(c)}" for c in columns])
        with self._get_cursor_object() as cur:
            if type(table) == str:
                cur.execute(f"alter {table} {add_statement}")
            elif isinstance(table, Table):
                cur.execute(f"{table.alter_statement()} {add_statement}")
            else:
                raise ValueError(f'Provided argument has to be Table object')

    def dev_console(self, sql: str) -> None:
        """ Utility made for custom development using sql syntax"""
        with self._get_cursor_object() as cur:
            cur.execute(str(sql))
            return cur.fetchall()

