from contextlib import contextmanager
from mysqlx import Error

from dbm_database_service.models.table import Table


class MySQLDatabaseManager:
    def __init__(self, connection_pool) -> None:
        self._connection_pool = connection_pool

    @contextmanager
    def _get_cursor_object(self):
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
        with self._get_cursor_object() as cur:
            cur.execute(str(table))
