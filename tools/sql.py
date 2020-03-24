import sqlparse


def default_sql(sql: str, keyword_case='upper', strip_comments=True) -> str:
    return sqlparse.format(
        sql=sql,
        encoding='utf-8',
        reindent=True,
        keyword_case=keyword_case,
        strip_comments=strip_comments
    ).strip().replace(chr(10), chr(32))


def determine_index(data: str) -> int:
    select = data.upper().find('SELECT')
    create = data.upper().find('CREATE')
    if select != -1 and create != -1:
        if select < create:
            return select
        return create
    if select != -1 and create == -1:
        return select
    return -1


if __name__ == '__main__':
    index = determine_index('acreatsesdfsdfsafasselect * from table')
    print(index)
