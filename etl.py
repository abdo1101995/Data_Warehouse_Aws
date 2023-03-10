import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    this function to load staging tables fron s3 bucket

    two args
        cur: the cursor
        conn:connection to database
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    this function to insert all data in tables fact and dimensions
    two args
        cur: the cursor
        conn:connection to database

    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    this func to implement all function in in order
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()