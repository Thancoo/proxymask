import sqlparse


def default_sql(sql: str, keyword_case='upper', strip_comments=True) -> str:
    return sqlparse.format(
        sql=sql,
        encoding='utf-8',
        reindent=True,
        keyword_case=keyword_case,
        strip_comments=strip_comments
    ).strip().replace(chr(10), chr(32))


def determine_index(data: bytes) -> int:
    select = data.upper().find(b'SELECT')
    create = data.upper().find(b'CREATE')
    if select != -1 and create != -1:
        if select < create:
            return select
        return create
    if select != -1 and create == -1:
        return select
    return -1


class Extractor:
    def __init__(self, sql_statement):
        self.sql = sqlparse.format(
            sql=sql_statement,
            reindent=True,
            keyword_case='upper'
        )
        self._table_names = set()
        self._alias_names = set()
        self._limit = None
        self._parsed = sqlparse.parse()

    def strip(self):
        return self.sql.strip(' \t\n')



if __name__ == '__main__':
    index = determine_index('acreatsesdfsdfsafasselect * from table')
    print(index)
