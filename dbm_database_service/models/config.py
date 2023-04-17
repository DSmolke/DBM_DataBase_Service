class Settings:
    valid_mysql_datatypes = [
        'INT', 'SMALLINT', 'TINYINT', 'MEDIUMINT',
        'BIGINT', 'ENUM',
        'BINARY', 'VARBINARY', 'BLOB',
        'DATE', 'TIME', 'DATETIME', 'TIMESTAMP',
        'YEAR', 'BOOLEAN', 'SET', 'JSON',
        'GEOMETRY', 'NULL', 'DECIMAL', 'FLOAT', 'DOUBLE',
        'CHAR', 'VARCHAR', 'TEXT'
    ]
    mysql_datatypes_without_corresponding_value = [
        'INT', 'SMALLINT', 'TINYINT', 'MEDIUMINT',
        'BIGINT', 'ENUM',
        'BINARY', 'VARBINARY', 'BLOB',
        'DATE', 'TIME', 'DATETIME', 'TIMESTAMP',
        'YEAR', 'BOOLEAN', 'SET', 'JSON',
        'GEOMETRY', 'NULL']

    mysql_datatypes_with_corresponding_value = ['DECIMAL', 'FLOAT', 'DOUBLE', 'CHAR', 'VARCHAR', 'TEXT']

