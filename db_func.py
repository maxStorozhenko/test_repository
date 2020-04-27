import sqlite3


def run_query(query: str) -> list:
    with sqlite3.connect('./chinook.db') as conn:
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        return results


def filter_and(query_param: str) -> str:
    query_params = query_param.split(';')
    if len(query_params) == 1:
        return f"{query_params[0].split(':')[0].capitalize()} = '{query_params[0].split(':')[1]}'"

    return f"""{query_params[0].split(':')[0].capitalize()} = '{query_params[0].split(':')[1]}' AND 
                {query_params[1].split(':')[0].capitalize()} = '{query_params[1].split(':')[1]}'"""
