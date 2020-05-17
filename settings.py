# Common

# 小于该字段不处理长度
LIMIT_LENGTH = 20

# 处理语句类型
QUERY_KEYS = ['select', 'from']

# 0 info
LEVEL = 0

# Oracle

# PgSQL

PG_REMOTE_ADDR = ('192.168.1.180', 5432)
PG_LOCAL_ADDR = ('192.168.1.180', 5432)


# 系统库
PGSQL_SYS_DATABASES = [
    'information_schema',
    'mysql',
    'performance_schema',
    'test',
    'scan_result'
]

# 不需要解析的库
PGSQL_PASS_KEYS = ['pg_', 'INFORMATION_SCHEMA']


# MySQL
# 系统库
MYSQL_SYS_DATABASES = [
    'information_schema',
    'mysql',
    'performance_schema',
    'test',
    'scan_result'
]

# 不需要解析的库
MYSQL_PASS_KEYS = ['information_schema']

