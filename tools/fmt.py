import sqlparse


def default_sql(statement: str, keyword_case='upper', strip_comments=True) -> str:
    return sqlparse.format(
        sql=statement,
        encoding='utf-8',
        reindent=True,
        keyword_case=keyword_case,
        strip_comments=strip_comments
    ).strip().replace(chr(10), chr(32))


def determine_index(data: bytes) -> int:
    """
    determine the location from common packet

    :param data: common packet, such as oracle, mysql
    :return: the index of sql statement
    """
    select = data.upper().find(b'SELECT')
    create = data.upper().find(b'CREATE')
    if select != -1 and create != -1:
        if select < create:
            return select
        return create
    if select != -1 and create == -1:
        return select
    return -1


if __name__ == '__main__':
    sql = '   select     *     from      node where       id =1 '
    print(default_sql(sql))
