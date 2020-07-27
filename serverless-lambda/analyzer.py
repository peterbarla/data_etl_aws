import os
import psycopg2
import sys

REDSHIFT_DATABASE = 'redshift-peter-1'
REDSHIFT_USER = 'peter.barla'
REDSHIFT_PASSWD = 'Pepecsek1'
REDSHIFT_PORT = '5439'
REDSHIFT_ENDPOINT = 'redshift-peter-1.cncdopxmun4t.us-east-2.redshift.amazonaws.com:5439/peterdb'

def build_and_send_query(category: str, filename: str, lwm: str, hwm: str, timestamp: str)-> str:

    # CREATING INSERT QUERY
    REDSHIFT_QUERY = ("INSERT INTO staging_uploaded_files VALUES(%s', %s', %s', %s', %s')", 
    (category, filename, lwm, hwm, timestamp))


    # CREATING A CONENCTION TO THE REDSHIFT CLUSTER
    try:
        conn = psycopg2.connect(
        dbname=REDSHIFT_DATABASE,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWD,
        port=REDSHIFT_PORT,
        host=REDSHIFT_ENDPOINT)
    except Exception as ERROR:
        print("Connection Issue: " + ERROR)
        sys.exit(1)

    # EXECUTING THE QUERY
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        print(cursor.execute(REDSHIFT_QUERY))
        cursor.close()
        conn.commit()
        conn.close()
    except Exception as ERROR:
        print("Execution Issue: " + ERROR)
        sys.exit(1)