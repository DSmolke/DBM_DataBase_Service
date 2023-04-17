import os
from typing import Self

from dotenv import load_dotenv
from easyvalid_data_validator.customexceptions.common import ValidationError
from easyvalid_data_validator.validator import validate_json_data
from easyvalid_data_validator.constraints import Constraint
from mysql.connector.pooling import MySQLConnectionPool

def get_connection_pool(absolute_dotenv_path: str | None = None) -> MySQLConnectionPool:
    """
    Function creates and returns connection pool for MySQLDatabase using variables stored in .env file
    :param absolute_dotenv_path: Filepath for file which stores MySQL DB credentials. If no file path is provided,
    function will use .env file from same place where is called
    :return: MySQLConnectorPool
    """
    """
        This env variables clearance is needed to avoid 'lost' 
        variables from previous loadings of .env if current one does not exist
    """
    for v in ['POOL_NAME', 'POOL_SIZE', 'POOL_RESET_SESSION', 'HOST', 'DATABASE', 'USER', 'PASSWORD', 'PORT']:
        if v in os.environ:
            del os.environ[v]
    load_dotenv(absolute_dotenv_path, override=True)
    try:
        return MySQLConnectionPool(
            pool_name=os.getenv('POOL_NAME'),
            pool_size=int(os.getenv('POOL_SIZE')),
            pool_reset_session=bool(os.getenv('POOL_RESET_SESSION')),
            host=os.getenv('HOST'),
            database=os.getenv('DATABASE'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=int(os.getenv('PORT'))
        )
    except TypeError:
        raise ConnectionError("File is invalid or doesn't exist")


class MySQLConnectionPoolBuilder:
    """ Builder of MySQLConnectionPool """
    def __init__(self, absolute_dotenv_path: str | None = None):

        # This env variables clearance is needed to avoid 'lost'
        # variables from previous loadings of .env if current one does not exist
        for v in ['POOL_NAME', 'POOL_SIZE', 'POOL_RESET_SESSION', 'HOST', 'DATABASE', 'USER', 'PASSWORD', 'PORT']:
            if v in os.environ:
                del os.environ[v]
        load_dotenv(absolute_dotenv_path, override=True)
        try:
            self._pool_config_ = {
                'pool_name': os.getenv('POOL_NAME'),
                'pool_size': int(os.getenv('POOL_SIZE')),
                'pool_reset_session': bool(os.getenv('POOL_RESET_SESSION')),
                'host': os.getenv('HOST'),
                'database': os.getenv('DATABASE'),
                'user': os.getenv('USER'),
                'password': os.getenv('PASSWORD'),
                'port': int(os.getenv('PORT'))
            }
            validate_json_data(self._pool_config_, constraints={
                'pool_name': {Constraint.IS_TYPE: str},
                'pool_size': {Constraint.IS_TYPE: int},
                'pool_reset_session': {Constraint.IS_TYPE: bool},
                'host': {Constraint.IS_TYPE: str},
                'database': {Constraint.IS_TYPE: str},
                'user': {Constraint.IS_TYPE: str},
                'password': {Constraint.IS_TYPE: str},
                'port': {Constraint.IS_TYPE: int},
            })
        except TypeError:
            raise ConnectionError("File is invalid or doesn't exist")

    def set_pool_name(self, new_pool_name: str) -> Self:
        """
        setter
        :param new_pool_name: new connection pool name
        :return: builder with new connection pool name
        """
        self._pool_config_['pool_name'] = new_pool_name
        return self

    def set_pool_size(self, new_pool_size: int) -> Self:
        """
        setter
        :param new_pool_size: new connection pool size
        :return: builder with new connection pool size
        """
        self._pool_config_['pool_size'] = new_pool_size
        return self

    def set_pool_reset_session(self, new_pool_reset_session: bool) -> Self:
        """
        setter
        :param new_pool_reset_session: new connection pool reset session value
        :return: builder with new connection pool reset session value
        """
        self._pool_config_['pool_reset_session'] = new_pool_reset_session
        return self

    def set_new_host(self, new_host: str) -> Self:
        """
        setter
        :param new_host: new connection host
        :return: builder with new connection host
        """
        self._pool_config_['host'] = new_host
        return self

    def set_new_database(self, new_database: str) -> Self:
        """
        setter
        :param new_database: new connection database
        :return: builder with new connection database
        """
        self._pool_config_['database'] = new_database
        return self

    def set_new_username(self, new_username: str) -> Self:
        """
        setter
        :param new_username: new connection username
        :return: builder with new connection username
        """
        self._pool_config_['user'] = new_username
        return self

    def set_new_password(self, new_user_password: str) -> Self:
        """
        setter
        :param new_user_password: new connection username password
        :return: builder with new connection username password
        """
        self._pool_config_['password'] = new_user_password
        return self

    def set_new_port(self, new_port: int) -> Self:
        """
        setter
        :param new_port: new connection port
        :return: builder with new connection port
        """
        self._pool_config_['port'] = new_port
        return self

    def build(self) -> MySQLConnectionPool:
        """ Validates created namespace, and tries to create MySQLConnectionPool. Can raise ConnectionError or ValidationError"""
        try:
            validate_json_data(self._pool_config_, constraints={
                'pool_name': {Constraint.IS_TYPE: str},
                'pool_size': {Constraint.IS_TYPE: int},
                'pool_reset_session': {Constraint.IS_TYPE: bool},
                'host': {Constraint.IS_TYPE: str},
                'database': {Constraint.IS_TYPE: str},
                'user': {Constraint.IS_TYPE: str},
                'password': {Constraint.IS_TYPE: str},
                'port': {Constraint.IS_TYPE: int},
            })
            return MySQLConnectionPool(**self._pool_config_)
        except TypeError:
            raise ConnectionError("File is invalid or doesn't exist")
        except ValidationError as e:
            raise ValidationError(e.args[0])
