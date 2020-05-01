import sqlite3


def run_query(query: str) -> list:
    with sqlite3.connect('./chinook.db') as conn:
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        return results


def filter_and(query_param: str) -> str:
    query_params = query_param.split(';')
    result = ''
    if query_params:
        for i in query_params:
            result += f"{i.split(':')[0].capitalize()} = '{i.split(':')[1]}' AND "

    return result[:-5]
